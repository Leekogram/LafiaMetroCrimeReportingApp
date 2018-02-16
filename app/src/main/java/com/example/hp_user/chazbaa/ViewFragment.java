package com.example.hp_user.chazbaa;

import android.app.Fragment;
import android.database.Cursor;
import android.graphics.drawable.BitmapDrawable;
import android.net.Uri;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

/**
 * Created by HP-USER on 2/11/2018.
 */

public class ViewFragment extends Fragment {
    private Cursor mCursor;
    private ImageView mImageView;

    @Override
    public void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);

        // Where is the photo object we want to show?
        int position = getArguments().getInt("Position");
// Load the appropriate photo from db
        DatabaseManager d = new DatabaseManager
                (getActivity().getApplicationContext());
        mCursor = d.getPhoto(position);
    }

    public View onCreateView(LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_view,
                container, false);
        TextView textView = (TextView)
                view.findViewById(R.id.textView);
        Button buttonShowLocation = (Button)
                view.findViewById(R.id.buttonShowLocation);
// Set the text from the tile column of the data.
        textView.setText(mCursor.getString
                (mCursor.getColumnIndex(DatabaseManager.TABLE_ROW_REPORTERNAME)));
        mImageView = (ImageView) view.findViewById(R.id.imageView);
// Load the image into the TextView via the URI
        mImageView.setImageURI(Uri.parse(mCursor.getString
                (mCursor.getColumnIndex(DatabaseManager.TABLE_ROW_URI))));
        return view;
    }
    public void onDestroy(){
        super.onDestroy();
// Make sure we don't run out of memory
        BitmapDrawable bd = (BitmapDrawable) mImageView.getDrawable();
        bd.getBitmap().recycle();
        mImageView.setImageBitmap(null);
    }
}
