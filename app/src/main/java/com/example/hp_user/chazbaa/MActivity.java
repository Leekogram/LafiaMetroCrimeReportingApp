package com.example.hp_user.chazbaa;

import android.app.Fragment;
import android.app.FragmentManager;
import android.content.res.Configuration;
import android.support.v4.view.GravityCompat;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.MenuItem;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ListView;

public class MActivity extends AppCompatActivity implements ActivityComs {


    private ListView mNavDrawerList;
    private DrawerLayout mDrawerLayout;
    private ArrayAdapter<String> mAdapter;
    private ActionBarDrawerToggle mDrawerToggle;
    private String mActivityTitle;
    public DatabaseManager dataManager;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_m);

        dataManager = new DatabaseManager(getApplicationContext());
// We will come back here in a minute!


        mActivityTitle = getTitle().toString();
    }
    private void switchFragment(int position) {
        Fragment fragment = null;
        String fragmentID ="";
        switch (position) {
            case 0:
                fragmentID = "TITLES";
                Bundle args = new Bundle();
                args.putString("Tag", "_NO_TAG");
                fragment = new TitlesFragment();
                fragment.setArguments(args);
                break;
            case 1:
                fragmentID = "TAGS";
                fragment = new TagsFragment();
                break;

            default:
                break;
        }
// More code goes here next
        FragmentManager fragmentManager = getFragmentManager();
        fragmentManager.beginTransaction()
                .replace(R.id.fragmentHolder, fragment,
                        fragmentID).commit();
        // Close the drawer
        mDrawerLayout.closeDrawer(mNavDrawerList);
    }

    @Override
    protected void onPostCreate(Bundle savedInstanceState) {
        super.onPostCreate(savedInstanceState);
        mDrawerToggle.syncState();
    }
    @Override
    public void onConfigurationChanged(Configuration newConfig) {
        super.onConfigurationChanged(newConfig);
        mDrawerToggle.onConfigurationChanged(newConfig);
    }
    @Override
    public void onBackPressed() {
// Close drawer if open
        if (mDrawerLayout.isDrawerOpen(GravityCompat.START)) {
//drawer is open so close it
            mDrawerLayout.closeDrawer(mNavDrawerList);
        }else {
// Go back to titles fragment
// Quit if already at titles fragment
            Fragment f = getFragmentManager().
                    findFragmentById(R.id.fragmentHolder);
            if (f instanceof TitlesFragment) {
                finish();
                System.exit(0);
            }else{
                switchFragment(0);
            }
        }
    }
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        int id = item.getItemId();
//noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }
// Activate the navigation drawer toggle
        if (mDrawerToggle.onOptionsItemSelected(item)) {
            return true;
        }
        return super.onOptionsItemSelected(item);
    }

    public void onTagsListItemSelected(String clickedTag) {
// We have just received a String for the TitlesFragment
// Prepare a new Bundle
        Bundle args = new Bundle();
// Pack the string into the Bundle
        args.putString("Tag", clickedTag);
        //  Create a new instance of TitlesFragment
        TitlesFragment fragment = new TitlesFragment();
// Load the Bundle into the Fragment
        fragment.setArguments(args);
// Start the fragment
        FragmentManager fragmentManager = getFragmentManager();
        fragmentManager.beginTransaction().replace
                (R.id.fragmentHolder, fragment, "TAGS").commit();
// update selected item and title, then close the drawer
        mNavDrawerList.setItemChecked(1, true);

        mNavDrawerList.setSelection(1);
        mDrawerLayout.closeDrawer(mNavDrawerList);

    }

    // Open ViewFragment with the photo indicated by position
    public void onTitlesListItemSelected(int position) {
// Load up the bundle with the row _id
        Bundle args = new Bundle();
        args.putInt("Position", position);
// Create the fragment and add the bundle
        ViewFragment fragment = new ViewFragment();
        fragment.setArguments(args);
// Start the fragment
        if (fragment != null) {
            FragmentManager fragmentManager = getFragmentManager();
            fragmentManager.beginTransaction().
                    replace(R.id.fragmentHolder, fragment, "VIEW").commit();
// update selected item and title, then close the drawer
            mNavDrawerList.setItemChecked(1, true);
            mNavDrawerList.setSelection(1);
//setTitle(navMenuTitles[position]);
            mDrawerLayout.closeDrawer(mNavDrawerList);
        } else {
// error in creating fragment
            Log.e("Activity", "Error in creating fragment");
        }
    }
}
