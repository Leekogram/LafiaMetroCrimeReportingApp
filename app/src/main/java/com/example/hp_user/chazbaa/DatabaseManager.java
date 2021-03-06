package com.example.hp_user.chazbaa;

import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

/**
 * Created by HP-USER on 2/11/2018.
 */

public class DatabaseManager {

    // This is the actual database
    private SQLiteDatabase db;
    /*
    Next we have a public static final string for
    each row/table that we need to refer to both
    inside and outside this class
    */
    public static final String TABLE_ROW_ID = "_id";
    public static final String TABLE_ROW_REPORTERNAME = "Reportername";
    public static final String TABLE_ROW_CRIMELOCATION = "Crimelocation";
    public static final String TABLE_ROW_CRIMEDESCRIPTION = "Crimedescription";
    public static final String TABLE_ROW_URI = "image_uri";

    // New with version 2
    public static final String TABLE_ROW_LOCATION_LAT = "gps_location_lat";
    public static final String TABLE_ROW_LOCATION_LONG = "gps_location_long";

    /*
Next we have a private static final strings for
each row/table that we need to refer to just
inside this class
*/
    private static final String DB_NAME = "crime_database";
    private static final int DB_VERSION = 2;
    private static final String TABLE_NAME = "crime_table";
    private static final String TABLE_TAGS = "table_tags";
    public static final String TABLE_ROW_TAG =
            "tag";// For the tags table


    public DatabaseManager(Context context) {
// Create an instance of our internal
//CustomSQLiteOpenHelper class
        CustomSQLiteOpenHelper helper =
                new CustomSQLiteOpenHelper(context);
// Get a writable database
        db = helper.getWritableDatabase();
    }

    // Here are all our helper methods
    // Insert a record
    public void insert(CrimeDetails crimeDetails) {
// Add all the details to the table
        String query = "INSERT INTO " + TABLE_NAME + " (" +
                TABLE_ROW_REPORTERNAME + ", " +
                TABLE_ROW_CRIMELOCATION + "," +
                TABLE_ROW_CRIMEDESCRIPTION +"," +
                TABLE_ROW_URI +","+
                TABLE_ROW_LOCATION_LAT + ", " +
                TABLE_ROW_LOCATION_LONG  +") " +
                "VALUES (" +
                "'" + crimeDetails.getReportername() + "'" + ", " +
                "'" + crimeDetails.getCrimelocation() + "'" + " ," +
                "'" + crimeDetails.getCrimedescription() + "'" +" ," +
                "'" + crimeDetails.getStorageLocation() + "'" +","+
                "'" + crimeDetails.getGpsLocation().getLatitude() + "'" +  ", "+
                "'" + crimeDetails.getGpsLocation().getLongitude()+ "'"  +
                "); ";

        db.execSQL(query);

        // Add any NEW tags to the tags table
        query = "INSERT INTO " + TABLE_TAGS + "(" +
                TABLE_ROW_TAG + ") " +
                "SELECT '" + crimeDetails.getReportername() + "' " +
                "WHERE NOT EXISTS ( SELECT 1 FROM " +
                TABLE_TAGS +
                " WHERE " + TABLE_ROW_TAG + " = " +
                "'" + crimeDetails.getReportername() + "');";
        db.execSQL(query);
        query = "INSERT INTO " + TABLE_TAGS + "(" +
                TABLE_ROW_TAG + ") " +
                "SELECT '" + crimeDetails.getCrimelocation() + "' " +
                "WHERE NOT EXISTS ( SELECT 1 FROM " +
                TABLE_TAGS +
                " WHERE " + TABLE_ROW_TAG + " = " +
                "'" + crimeDetails.getCrimelocation() + "');";
        db.execSQL(query);
        query = "INSERT INTO " + TABLE_TAGS + "(" +
                TABLE_ROW_TAG + ") " +
                "SELECT '" + crimeDetails.getCrimedescription() + "' " +
                "WHERE NOT EXISTS ( SELECT 1 FROM " +
                TABLE_TAGS +
                " WHERE " + TABLE_ROW_TAG + " = " +
                "'" + crimeDetails.getCrimedescription() + "');";
        db.execSQL(query);

    }

    public Cursor getTitles() {
        Cursor c = db.rawQuery("SELECT " + TABLE_ROW_ID + ", "
                + TABLE_ROW_REPORTERNAME + " from " + TABLE_NAME, null);
        c.moveToFirst();
        return c;
    }

    public Cursor getTitlesWithTag(String tag) {
        Cursor c = db.rawQuery("SELECT " + TABLE_ROW_ID + ", " +
                        TABLE_ROW_REPORTERNAME + " from " +
                         " WHERE " +
                        TABLE_ROW_CRIMELOCATION + " = '" + tag + "' or " +
                        TABLE_ROW_CRIMEDESCRIPTION + " = '" + tag + "';"
                , null);
        c.moveToFirst();
        return c;
    }
    public Cursor getReporter(int id) {
        Cursor c = db.rawQuery("SELECT * from " +
                TABLE_NAME +
                " WHERE " +
                TABLE_ROW_ID + " = " + id, null);
        c.moveToFirst();
        return c;
    }

    public Cursor getPhoto(int id) {
        Cursor c = db.rawQuery("SELECT * from " +
                TABLE_NAME +
                " WHERE " +
                TABLE_ROW_ID + " = " + id, null);
        c.moveToFirst();
        return c;
    }

    public Cursor getTags(){
        Cursor c = db.rawQuery("SELECT " + TABLE_ROW_ID + ", "
                + TABLE_ROW_TAG + " from " + TABLE_TAGS, null);
                c.moveToFirst();
        return c;
    }

    // This class is created when our DataManager is initialized
    private class CustomSQLiteOpenHelper extends SQLiteOpenHelper {
        public CustomSQLiteOpenHelper(Context context) {
            super(context, DB_NAME, null, DB_VERSION);
        }

        // This method only runs the first time the database is created
        @Override
        public void onCreate(SQLiteDatabase db) {
// Create a table for photos and all their details
            String newTableQueryString = "create table "
                    + TABLE_NAME + " ("
                    + TABLE_ROW_ID
                    + " integer primary key autoincrement not null,"
                    + TABLE_ROW_REPORTERNAME
                    + " text not null,"
                    + TABLE_ROW_CRIMELOCATION
                    + " text not null,"
                    + TABLE_ROW_CRIMEDESCRIPTION
                    + " text not null,"
                    + TABLE_ROW_URI
                    + " text not null,"
                    + TABLE_ROW_LOCATION_LAT
                    + " real,"
                    + TABLE_ROW_LOCATION_LONG
                    + " real"+ ");";
            db.execSQL(newTableQueryString);


// Create a separate table for tags
            // Create a separate table for tags
            newTableQueryString = "create table "
                    + TABLE_TAGS + " ("
                    + TABLE_ROW_ID
                    + " integer primary key autoincrement not null,"
                    + TABLE_ROW_TAG
                    + " text not null" + ");";
            db.execSQL(newTableQueryString);

        }

        // This method only runs when we increment DB_VERSION
        @Override
        public void onUpgrade(SQLiteDatabase db,
                              int oldVersion, int newVersion) {
            // Update for version 2
            String addLongColumn = "ALTER TABLE " +
                    TABLE_NAME +
                    " ADD " +
                    TABLE_ROW_LOCATION_LONG +
                    " real;";
            db.execSQL(addLongColumn);
            String addLatColumn = "ALTER TABLE " +
                    TABLE_NAME + " ADD " +
                    TABLE_ROW_LOCATION_LAT +
                    " real;";
            db.execSQL(addLatColumn);

        }

    }
}