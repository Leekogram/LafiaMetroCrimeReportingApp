package com.example.hp_user.chazbaa;

import android.location.Location;
import android.net.Uri;

/**
 * Created by HP-USER on 2/11/2018.
 */

public class CrimeDetails {

    private String mReportername;
    private Uri mStorageLocation;
    private String mCrimelocation;
    private String mCrimedescription;
    private Location mGpsLocation;

    public Location getGpsLocation() {
        return mGpsLocation;
    }

    public void setGpsLocation(Location mGpsLocation) {
        this.mGpsLocation = mGpsLocation;
    }

    public String getReportername() {
        return mReportername;
    }

    public void setReportername(String mReportername) {
        this.mReportername = mReportername;
    }

    public Uri getStorageLocation() {
        return mStorageLocation;
    }

    public void setStorageLocation(Uri mStorageLocation) {
        this.mStorageLocation = mStorageLocation;
    }

    public String getCrimelocation() {
        return mCrimelocation;
    }

    public void setCrimelocation(String mCrimelocation) {
        this.mCrimelocation = mCrimelocation;
    }

    public String getCrimedescription() {
        return mCrimedescription;
    }

    public void setCrimedescription(String mCrimedescription) {
        this.mCrimedescription = mCrimedescription;
    }
}
