package com.example.hp_user.chazbaa;

import android.app.Activity;
import android.app.ListFragment;
import android.database.Cursor;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ListView;
import android.widget.SimpleCursorAdapter;

/**
 * Created by HP-USER on 2/11/2018.
 */

public class TagsFragment extends ListFragment {
    private ActivityComs mActivityComs;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        DatabaseManager d = new DatabaseManager
                (getActivity().getApplicationContext());
        Cursor c = d.getTags();
// Create a new adapter
        SimpleCursorAdapter cursorAdapter =
                new SimpleCursorAdapter(getActivity(),
                        android.R.layout.simple_list_item_1, c,
                        new String[] { DatabaseManager.TABLE_ROW_TAG },
                        new int[] { android.R.id.text1 }, 0);
// Attach the Cursor to the adapter
        setListAdapter(cursorAdapter);
    }

    public void onListItemClick(ListView l, View v,
                                int position, long id) {
// What tag has just been clicked?
        Cursor c = ((SimpleCursorAdapter)l.getAdapter()).getCursor();
        c.moveToPosition(position);
        String clickedTag = c.getString(1);
// 1 is the position of the string
        Log.e("clickedTag = ", " " + clickedTag);
        mActivityComs.onTagsListItemSelected(clickedTag);
    }
    @Override
    public void onAttach(Activity activity) {
        super.onAttach(activity);
        mActivityComs = (ActivityComs)activity;
    }
    @Override
    public void onDetach() {
        super.onDetach();
        mActivityComs = null;
    }

}
