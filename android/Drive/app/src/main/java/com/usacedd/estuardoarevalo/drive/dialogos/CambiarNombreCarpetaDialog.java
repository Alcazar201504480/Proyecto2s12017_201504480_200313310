package com.usacedd.estuardoarevalo.drive.dialogos;
import android.app.Activity;
import android.app.Dialog;
import android.content.DialogInterface;
import android.os.Bundle;
import android.support.v4.app.DialogFragment;
import android.support.v7.app.AlertDialog;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.EditText;


import com.usacedd.estuardoarevalo.drive.R;

/**
 * Created by estuardoarevalo on 5/7/17.
 */

public class CambiarNombreCarpetaDialog extends DialogFragment
{
    public static final String ARG_TITLE = "CambiarNombreCarpetaDialog.Title";
    public static final String ARG_MESSAGE = "CambiarNombreCarpetaDialog.Message";
    public static final String ARG_ACTION = "CambiarNombreCarpetaDialog.Action";
    public static final String ARG_CARPETA = "CambiarNombreCarpetaDialog.Carpeta";
    public static final String ARG_TIPO = "CambiarNombreCarpetaDialog.Tipo";

    @Override
    public Dialog onCreateDialog(Bundle savedInstanceState)
    {
        Bundle args = getArguments();
        String title = args.getString(ARG_TITLE);
        String message = args.getString(ARG_MESSAGE);
        final int action = args.getInt(ARG_ACTION);
        final  String carpeta = args.getString(ARG_CARPETA);
        final int tipo = args.getInt(ARG_TIPO);

        LayoutInflater inflater = getActivity().getLayoutInflater();
        View view = inflater.inflate(R.layout.nombre_carpeta, null);

        return new AlertDialog.Builder(getActivity())
                .setTitle(title)
                .setView(view)
                .setMessage(message)
                .setPositiveButton(android.R.string.yes, new DialogInterface.OnClickListener()
                {
                    @Override
                    public void onClick(DialogInterface dialog, int which)
                    {
                        EditText editText = (EditText) getDialog().findViewById(R.id.dialogo_nombre_carpeta);
                        // Send the positive button event back to the host activity
                        mListener.onDialogPositiveClick(CambiarNombreCarpetaDialog.this, action, tipo, carpeta, editText.getText().toString());
                    }
                })
                .setNegativeButton(android.R.string.no, new DialogInterface.OnClickListener()
                {
                    @Override
                    public void onClick(DialogInterface dialog, int which)
                    {
                        // Send the negative button event back to the host activity
                        mListener.onDialogNegativeClick(CambiarNombreCarpetaDialog.this);
                    }
                })
                .create();
    }

    /* The activity that creates an instance of this dialog fragment must
     * implement this interface in order to receive event callbacks.
     * Each method passes the DialogFragment in case the host needs to query it. */
    public interface NoticeDialogListener {
        public void onDialogPositiveClick(DialogFragment dialog, int action, int tipo, String carpeta, String inputText);
        public void onDialogNegativeClick(DialogFragment dialog);
    }

    // Use this instance of the interface to deliver action events
    NoticeDialogListener mListener;

    // Override the Fragment.onAttach() method to instantiate the NoticeDialogListener
    @Override
    public void onAttach(Activity activity) {
        super.onAttach(activity);
        // Verify that the host activity implements the callback interface
        try {
            // Instantiate the NoticeDialogListener so we can send events to the host
            mListener = (NoticeDialogListener) activity;
        } catch (ClassCastException e) {
            // The activity doesn't implement the interface, throw exception
            throw new ClassCastException(activity.toString()
                    + " must implement NoticeDialogListener");
        }
    }

}

