package com.example.hp_user.chazbaa;

import android.app.AlertDialog;
import android.app.Dialog;
import android.app.DialogFragment;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.ImageButton;

/**
 * Created by HP-USER on 2/8/2018.
 */

public class Dialog_calling extends DialogFragment {

    @Override
    public Dialog onCreateDialog(Bundle savedInstanceState){

        AlertDialog.Builder builder = new AlertDialog.Builder(getActivity());
        LayoutInflater inflater = getActivity().getLayoutInflater();
        View dialogView = inflater.inflate(R.layout.dailog_call, null);

        builder.setView(dialogView).setMessage("Make Sos Call");

        ImageButton btnCallPolice=(ImageButton)dialogView.findViewById(R.id.btnCallCops);
        ImageButton btnCallAmb =(ImageButton)dialogView.findViewById(R.id.btnAmbulance);
        ImageButton btnCallFire =(ImageButton)dialogView.findViewById(R.id.btnCallFireStation);


        btnCallPolice.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent callIntentpolice = new Intent(Intent.ACTION_DIAL);
                callIntentpolice.setData(Uri.parse("tel:123456789"));
                startActivity(callIntentpolice);

            }
        });

        btnCallAmb.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent callIntentambulance = new Intent(Intent.ACTION_DIAL);
                callIntentambulance.setData(Uri.parse("tel:1234"));
                startActivity(callIntentambulance);

            }
        });

        btnCallFire.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent callIntentfireservice = new Intent(Intent.ACTION_DIAL);
                callIntentfireservice.setData(Uri.parse("tel:1234"));
                startActivity(callIntentfireservice);

            }
        });









        return builder.create();
    }
}
