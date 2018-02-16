package com.example.hp_user.chazbaa;

import android.app.AlertDialog;
import android.app.Dialog;
import android.app.DialogFragment;
import android.content.Context;
import android.location.Criteria;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.TextView;

/**
 * Created by HP-USER on 2/11/2018.
 */

public class GetLocation extends DialogFragment implements LocationListener {

    private TextView txtLat;
    private TextView txtLong;
    private TextView txtSource;
    private LocationManager locationManager;
    private String provider;

    @Override
    public Dialog onCreateDialog(Bundle savedInstanceState) {

        AlertDialog.Builder builder = new AlertDialog.Builder(getActivity());
        LayoutInflater inflater = getActivity().getLayoutInflater();
        View getlocatn = inflater.inflate(R.layout.position_layout, null);

        builder.setView(getlocatn).setMessage("Get Location");

        txtLat = (TextView) getlocatn.findViewById(R.id.txtLat);
        txtLong = (TextView) getlocatn.findViewById(R.id.txtLong);
        txtSource = (TextView) getlocatn.findViewById(R.id.txtSource);
// Initialize locationManager
        locationManager = (LocationManager) getActivity(). getSystemService(Context.LOCATION_SERVICE);
        Criteria criteria = new Criteria();
        provider = locationManager.getBestProvider(criteria, false);
        Location location = locationManager.
                getLastKnownLocation(provider);
// Initialize the location
        if (location != null) {
            txtSource.setText("Source = " + provider);
            onLocationChanged(location);
        }








        return builder.create();
    }
    // Start updates when app starts/resumes
    @Override
    public void onResume() {
        super.onResume();
        locationManager.requestLocationUpdates
                (provider, 500, 1, this);
    }
    @Override
    public void onPause() {
        super.onPause();
        locationManager.removeUpdates(this);
    }

    @Override
    public void onLocationChanged(Location location) {
        double lat = location.getLatitude();
        double lng = location.getLongitude();
        txtLat.setText(String.valueOf(lat));
        txtLong.setText(String.valueOf(lng));
        txtSource.setText("Source = " + provider);
    }
    @Override
    public void onStatusChanged(String provider,
                                int status, Bundle extras) {
        txtSource.setText("Source = " + provider);
    }
    @Override
    public void onProviderEnabled(String provider) {
        txtSource.setText("Source = " + provider);
    }
    @Override
    public void onProviderDisabled(String provider) {
        txtSource.setText("Source = " + provider);
    }

}