package com.che.helloworld;

import java.io.IOException;
import java.io.InputStream;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.HashMap;

import android.content.Context;
import android.graphics.drawable.Drawable;
import android.os.AsyncTask;
import android.util.Log;
import android.widget.BaseAdapter;
import android.widget.ImageView;

class ImageWorker {
    private HashMap<String, Drawable> imageCache; // 使用缓存，避免重复下载
    private static final Drawable DEFAULT_ICON = null;
    private BaseAdapter adapt;

    ImageWorker(Context ctx) {
        imageCache = new HashMap<String, Drawable>();
    }

    Drawable loadImage(BaseAdapter adapt, ImageView view) {
        this.adapt = adapt;
        String url = (String) view.getTag();

        if (imageCache.containsKey(url)) {
            return imageCache.get(url);
        } else {
            synchronized (this) {
                imageCache.put(url, DEFAULT_ICON); // 存入缓存
            }
            new ImageTask().execute(url); // 开启任务
            return DEFAULT_ICON;
        }
    }

    private class ImageTask extends AsyncTask<String, Void, Drawable> { // ImageTask的异步任务
        private String s_url;

        @Override
        protected Drawable doInBackground(String... params) {
            s_url = params[0];
            InputStream istr;

            try {
                URL url = new URL(s_url);
                //HttpsURLConnection conn = (HttpsURLConnection)url.openConnection();
                //istr = conn.getInputStream(); // 出错了？
                istr = url.openStream();

            } catch (MalformedURLException e) {
                Log.d("Che", "Malformed: " + e.getMessage());
                throw new RuntimeException(e);
            } catch (IOException e) {
                Log.d("Che", "I/O : " + e.getMessage());
                throw new RuntimeException(e);
            }

            return Drawable.createFromStream(istr, "src");
        }

        @Override
        protected void onPostExecute(Drawable result) {
            super.onPostExecute(result);
            synchronized (this) {
                imageCache.put(s_url, result);
            }
            adapt.notifyDataSetChanged();  // 必须, 通知JsonAdapter状态改变, 更新视图
        }
    }
}
