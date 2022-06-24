package com.che.helloworld;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import android.content.Context;
import android.content.Intent;
import android.graphics.drawable.Drawable;
import android.net.Uri;
import android.os.AsyncTask;
import android.os.Bundle;
import android.text.util.Linkify;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.view.View.OnClickListener;
import android.view.inputmethod.InputMethodManager;
import android.widget.BaseAdapter;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.util.concurrent.TimeUnit;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class MainActivity extends AppCompatActivity {
    static final private int EXIT_ID = Menu.FIRST;

    private EditText m_search_key;
    private ImageButton m_btn_ok;
    private TextView m_header;
    private ListView m_tweet_list;
    private InputMethodManager im_ctrl;
    private JSONArray tweets;
    private LayoutInflater m_inflater;  // 为了布局更灵活？
    private ImageWorker iw;


    /**
     * 正则过滤模式
     */

    /* Pattern for matching from_user */
    private Pattern fromUserPat = Pattern.compile("^[A-Za-z0-9_]+");

    /* Pattern for matching @user */
    private Pattern userPat = Pattern.compile("@[A-Za-z0-9_]+");

    /* Pattern for matching #searchkey */
    private Pattern hashPat = Pattern.compile("#[A-Za-z0-9_]+");

    /* Pattern for matching URL, Linkify.WEB_URLS seem to overdo the substitution */
    private Pattern urlPat = Pattern.compile("http://[^ ]+");

    private String twitUserURL = "http://twitter.com/";
    private String twitSearchURL = "http://search.twitter.com/search?q=";

    /**
     * Called when the activity is first created.
     */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        /* Use res/layout/main.xml as the view of
         * this Activity */
        setContentView(R.layout.activity_main);
        m_search_key = findViewById(R.id.search_key);
        m_btn_ok = findViewById(R.id.btn_ok);
        m_tweet_list = findViewById(R.id.tweet_list);
        m_header = findViewById(R.id.tweet_header);
        m_btn_ok.setOnClickListener(ok_handler);

        im_ctrl = (InputMethodManager) getSystemService(Context.INPUT_METHOD_SERVICE);
        m_inflater = LayoutInflater.from(this);

        iw = new ImageWorker(this);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        super.onCreateOptionsMenu(menu);

        /* the context menu currently has only one option */
        menu.add(0, EXIT_ID, 0, R.string.exit);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        switch (item.getItemId()) {
            case EXIT_ID:
                finish(); /* terminate the application */
                return true;
        }
        return super.onOptionsItemSelected(item);
    }

    private void alert(String msg) {
        Toast.makeText(getApplicationContext(), msg, Toast.LENGTH_LONG).show();
    }

    OnClickListener ok_handler = new OnClickListener() {
        @Override
        public void onClick(View v) {
            im_ctrl.hideSoftInputFromWindow(m_search_key.getWindowToken(), 0);
            TwitterTask twit_task = new TwitterTask();

            try {
                /* get 100 most recent tweets */
                // 触发任务
                twit_task.execute("?per_page=50&q=" + Uri.encode(m_search_key.getText().toString()));
                twit_task.get(90, TimeUnit.SECONDS);
            } catch (Exception e) {
                twit_task.cancel(true);
                alert("Cannot retrieve tweets...");
            }

        }
    };

    /* Params (String), Progress (Integer), Result (String) */
    // 内部后台任务
    private class TwitterTask extends AsyncTask<String, Integer, String> {
        @Override
        protected void onPreExecute() {
            super.onPreExecute();
        }

        @Override
        protected String doInBackground(String... params) {
            try {
                String result = TwitterHelper.downloadFromServer(params[0]);
                return result;
            } catch (Exception e) {
                return "";
            }
        }

        @Override
        protected void onPostExecute(String result) {
            if (result.length() == 0) {
                alert("Connection Problem?");
                return;
            }

            try {
                JSONObject obj = new JSONObject(result);
                tweets = obj.getJSONArray("items");

                if (tweets == null || tweets.length() == 0) {
                    Toast.makeText(getApplicationContext(), "No tweets on " + m_search_key.getText(), Toast.LENGTH_LONG).show();
                } else {
                    m_tweet_list.setAdapter(new JSONAdapter(getApplicationContext())); // 连接点
                }
            } catch (JSONException e) {
                alert("onPostExecute(): " + e.getMessage());
            }

        }
    }

    /**
     * 链接处理类
     */
    private Linkify.TransformFilter noAtSign = new Linkify.TransformFilter() {

        /* A Filter to remove the @ character before the user name */
        @Override
        public String transformUrl(Matcher match, String user) {
            return user.substring(1);
        }
    };

    private Linkify.TransformFilter hashEncoder = new Linkify.TransformFilter() {

        /* A Filter to remove the @ character before the user name */
        @Override
        public String transformUrl(Matcher match, String hash) {
            return Uri.encode(hash);
        }
    };

    // 内部存储类
    static class ViewHolder {
        TextView text, time;
        ImageView icon;
    }

    /*--- ListAdapter for rendering JSON data ---*/
    private class JSONAdapter extends BaseAdapter {
        JSONAdapter(Context c) {
        }

        @Override
        public int getCount() { // key1
            return tweets == null ? 0 : tweets.length();
        }

        @Override
        public Object getItem(int arg0) {
            return null;
        }

        @Override
        public long getItemId(int pos) {
            return pos;
        }

        @Override
        public View getView(int pos, View convertView, ViewGroup parent) {  // key2
            // convertView回收利用的View
            ImageView photo;
            ViewHolder holder;

            if (convertView == null) {
                convertView = m_inflater.inflate(R.layout.item, parent, false);

                // holder里存储目标的引用
                holder = new ViewHolder();
                holder.text = convertView.findViewById(R.id.text);
                holder.time = convertView.findViewById(R.id.created_at);
                holder.icon = convertView.findViewById(R.id.user_photo);
                convertView.setTag(holder);
            } else {
                holder = (ViewHolder) convertView.getTag();
            }

            try {
                JSONObject obj = tweets.getJSONObject(pos);

                TextView t = holder.text;
                t.setText(obj.getString("full_name") + ": " + obj.getString("description"));
                Linkify.addLinks(t, fromUserPat, twitUserURL);
                Linkify.addLinks(t, userPat, twitUserURL, null, noAtSign);
                Linkify.addLinks(t, hashPat, twitSearchURL, null, hashEncoder);
                Linkify.addLinks(t, urlPat, "");

                photo = holder.icon;
                JSONObject o = obj.getJSONObject("owner");
                photo.setTag(o.getString("avatar_url"));
                Drawable dr = iw.loadImage(this, photo); // 下载图片
                photo.setImageDrawable(dr);

                holder.time.setText(obj.getString("created_at"));
            } catch (JSONException e) {
                Log.e("Che", "Error in getView(): " + e.getMessage());
            }

            return convertView;  // 直接返回这里，怎么渲染的?
        }
    }
}
