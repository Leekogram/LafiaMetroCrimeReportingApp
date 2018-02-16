package com.example.hp_user.chazbaa;

import android.app.AlertDialog;
import android.app.Dialog;
import android.app.DialogFragment;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.Button;

/**
 * Created by HP-USER on 2/10/2018.
 */

public class Setup_profile extends DialogFragment {
    @Override
    public Dialog onCreateDialog(Bundle onsavedInstanceState){

        AlertDialog.Builder builder = new AlertDialog.Builder(getActivity());
        LayoutInflater inflater = getActivity().getLayoutInflater();
        View dialog = inflater.inflate(R.layout.setup_profile, null);

        builder.setView(dialog).setMessage("Sign up ");

        Button signup =(Button)dialog.findViewById(R.id.btnsignup);

        signup.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

            }
        });

        return builder.create();


    }


}
