package com.example.hp_user.chazbaa;

import android.app.Activity;
import android.app.AlertDialog;
import android.app.Dialog;
import android.app.DialogFragment;
import android.content.Context;
import android.content.Intent;
import android.graphics.drawable.BitmapDrawable;
import android.location.Criteria;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.provider.MediaStore;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Toast;

import java.io.File;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * Created by HP-USER on 2/7/2018.
 */

public class ReportIncidents extends DialogFragment implements LocationListener{
    private static final int CAMERA_REQUEST = 123;
    private ImageView mImageView;
    // Where the captured image is stored
    private Uri mImageUri = Uri.EMPTY;
    // Where to save the image
    String mCurrentPhotoPath;

    // A reference to our database
    private DatabaseManager mDatabaseManager;
    // For the Location
    private Location mLocation = new Location("");
    private LocationManager mLocationManager;
    private String mProvider;

    @Override
    public Dialog onCreateDialog(Bundle savedInstanceState){

        AlertDialog.Builder builder = new AlertDialog.Builder(getActivity());
        LayoutInflater inflater = getActivity().getLayoutInflater();
        View dialogView = inflater.inflate(R.layout.reportincidents, null);

        builder.setView(dialogView).setMessage("Report crime");
        mDatabaseManager =
                new DatabaseManager(getActivity()
                        .getApplicationContext());
        // Initialize mLocationManager
        mLocationManager = (LocationManager)
                getActivity().getSystemService(Context.LOCATION_SERVICE);
        Criteria criteria = new Criteria();
        mProvider = mLocationManager.getBestProvider(criteria, false);

        mImageView = (ImageView)dialogView.findViewById(R.id.imageView);
        Button btnCapture = (Button)dialogView.findViewById(R.id.btnCapture);
        Button btnSave =(Button)dialogView.findViewById(R.id.btnSubmit);



        final EditText mReporterTitle =
                (EditText)dialogView.findViewById(R.id.txtReportername);
        final EditText mCrimelocation =
                (EditText)dialogView.findViewById(R.id.txtCrimelocation);
        final EditText mCrimedescription =
                (EditText)dialogView.findViewById(R.id.txtCrimedescritpion);




        btnCapture.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent cameraIntent =
                        new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
                File photoFile = null;
                try {
                    photoFile = createImageFile();
                } catch (IOException ex) {
// Error occurred while creating the File
                    Log.e("error", "error creating file");
                }
// Continue only if the File was successfully created
                if (photoFile != null) {
                    mImageUri = Uri.fromFile(photoFile);
                    cameraIntent.putExtra(MediaStore.EXTRA_OUTPUT,
                            Uri.fromFile(photoFile));
                    startActivityForResult(cameraIntent, CAMERA_REQUEST);
                }

            }
        });



        // Listen for clicks on the save button
        btnSave.setOnClickListener(new View.OnClickListener() {
                                       @Override
                                       public void onClick(View v) {

                                           if (mImageUri != null) {
                                               if (!mImageUri.equals(Uri.EMPTY)) {

                                                   CrimeDetails cd = new CrimeDetails();

                                                   String tag1 = mReporterTitle.getText().toString();
                                                   String tag2 = mCrimelocation.getText().toString();
                                                   String tag3 = mCrimedescription.getText().toString();
// Assign the strings to the Photo object
                                                   cd.setReportername(tag1);
                                                   cd.setCrimelocation(tag2);
                                                   cd.setCrimedescription(tag3);
                                                   cd.setStorageLocation(mImageUri);
                                                   // Set the current GPS location
                                                   cd.setGpsLocation(mLocation);

                                                   // Send the new object to our DataManager
                                                   mDatabaseManager.insert(cd);
                                                   Toast.makeText(getActivity(), "Saved", Toast.LENGTH_LONG).
                                                           show();


                                               } else {
// No image
                                                   Toast.makeText(getActivity(), "No image to save", Toast.
                                                           LENGTH_LONG).show();
                                               }
                                           } else {
// Uri not initialized
                                               Toast.makeText(getActivity(), "Uri empty", Toast.
                                                       LENGTH_LONG).show();
                                           }
                                       }
                                   });


// We have a photo to save


        return builder.create();
    }
    private File createImageFile() throws IOException {
// Create an image file name
        String timeStamp = new SimpleDateFormat
                ("yyyyMMdd_HHmmss").format(new Date());
        String imageFileName = "JPEG_" + timeStamp + "_";
        File storageDir = Environment.getExternalStoragePublicDirectory(
                Environment.DIRECTORY_PICTURES);
        File image = File.createTempFile(
                imageFileName, // filename
                ".jpg", // extension
                storageDir // folder
        );
// Save for use with ACTION_VIEW Intent
        mCurrentPhotoPath = "file:" + image.getAbsolutePath();
        return image;
    }
    @Override
    public void onActivityResult
            (int requestCode, int resultCode, Intent data) {
        if (requestCode == CAMERA_REQUEST &&
                resultCode == Activity.RESULT_OK) {
            try {
                mImageView.setImageURI(Uri.parse(mImageUri.toString()));
            }catch(Exception e){
                Log.e("Error","Uri not set");
            }
        }else{
            mImageUri = Uri.EMPTY;
        }
    }
    public void onDestroy(){
        super.onDestroy();
// Make sure we don't run out of memory
        BitmapDrawable bd = (BitmapDrawable) mImageView.getDrawable();
        bd.getBitmap().recycle();
        mImageView.setImageBitmap(null);
    }
    @Override
    public void onLocationChanged(Location location) {
// Update the location if it changed
        mLocation = location;
    }
    @Override
    public void onStatusChanged(String provider,
                                int status, Bundle extras) {
    }
    @Override
    public void onProviderEnabled(String provider) {
    }
    @Override
    public void onProviderDisabled(String provider) {
    }
    // Start updates when app starts/resumes
    @Override
    public void onResume() {
        super.onResume();
        mLocationManager.requestLocationUpdates
                (mProvider, 500, 1, this);
    }
// pause the location manager when app is paused/stopped
    @Override
    public void onPause() {
        super.onPause();
        mLocationManager.removeUpdates(this);
    }
}
