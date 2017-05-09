package com.usacedd.estuardoarevalo.drive.utilidades;

import android.content.Context;
import android.content.SharedPreferences;

import com.google.gson.FieldNamingPolicy;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.internal.bind.DateTypeAdapter;
import com.usacedd.estuardoarevalo.drive.modelos.SesionUsuario;

import java.util.Date;

/**
 * Created by estuardoarevalo on 3/28/17.
 */

public class Preferencias {

    /**
     * Used for debugging.
     */
    private final static String TAG = "Preferences";

    /**
     * Nombre de la lista de Shared Preferences de Smart Communication Manager
     */
    public static final String PREFERENCIA = "drive.sharedpreferences";
    public static final String PREFERENCIA_SESION = "drive.sharedpreferences.sesion";

    public static void guardarSesionUsuario(Context context, SesionUsuario sesionUsuario){

        SharedPreferences settings = context.getSharedPreferences(PREFERENCIA, 0);
        SharedPreferences.Editor editor = settings.edit();

        Gson gson = new GsonBuilder()
                .setFieldNamingPolicy(FieldNamingPolicy.LOWER_CASE_WITH_UNDERSCORES)
                .registerTypeAdapter(Date.class, new DateTypeAdapter())
                .setDateFormat("yyyy-MM-dd'T'HH:mm:ss")
                .create();

        String jsonUserSession = gson.toJson(sesionUsuario);

        editor.putString(PREFERENCIA_SESION, jsonUserSession);

        editor.commit();
    }

    public static void borrarSesionUsuario(Context context){

        SharedPreferences settings = context.getSharedPreferences(PREFERENCIA, 0);
        SharedPreferences.Editor editor = settings.edit();
        editor.putString(PREFERENCIA_SESION, "");
        editor.commit();
    }

    public static SesionUsuario getSesionUsuario(Context context){

        SesionUsuario sesionUsuario;

        SharedPreferences settings = context.getSharedPreferences(PREFERENCIA, 0);
        String jsonUserSession = settings.getString(PREFERENCIA_SESION,"");

        //si no hay almacenado nada devolver null
        if (jsonUserSession.equals("")) return null;

        Gson gson = new GsonBuilder()
                .setFieldNamingPolicy(FieldNamingPolicy.LOWER_CASE_WITH_UNDERSCORES)
                .registerTypeAdapter(Date.class, new DateTypeAdapter())
                .setDateFormat("yyyy-MM-dd'T'HH:mm:ss")
                .create();

        sesionUsuario = gson.fromJson(jsonUserSession, SesionUsuario.class);

        return sesionUsuario;

    }

}
