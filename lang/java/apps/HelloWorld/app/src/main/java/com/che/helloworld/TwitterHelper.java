package com.che.helloworld;

import java.io.ByteArrayOutputStream;
import java.io.InputStream;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.StatusLine;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;

import android.net.Uri;

public class TwitterHelper {

    private static final String TWITTER_SEARCH = "https://api.github.com/search/repositories";
    private static final int HTTP_STATUS_OK = 200;
    private static byte[] buff = new byte[1024];

    static class ApiException extends Exception {
        ApiException(String msg) {
            super(msg);
        }

        ApiException(String msg, Throwable thr) {
            super(msg, thr);
        }
    }

    public static class ParseException extends Exception {
        public ParseException(String msg, Throwable thr) {
            super(msg, thr);
        }
    }

    //
    static synchronized String downloadFromServer(String keyword)
            throws ApiException {
        String url = TWITTER_SEARCH + keyword;
        HttpClient client = new DefaultHttpClient();
        HttpGet request = new HttpGet(url);
        try {
            HttpResponse response = client.execute(request); // 开始下载数据
            StatusLine status = response.getStatusLine();
            if (status.getStatusCode() != HTTP_STATUS_OK)
                throw new ApiException("Invalid response from search.twitter.com" + status.toString());

            HttpEntity entity = response.getEntity();
            InputStream ist = entity.getContent();
            ByteArrayOutputStream content = new ByteArrayOutputStream();

            int readCount = 0;
            while ((readCount = ist.read(buff)) != -1)
                content.write(buff, 0, readCount);
            return new String(content.toByteArray());

        } catch (Exception e) {
            e.printStackTrace();
            throw new ApiException("Problem using the API", e);
        }
    }
}