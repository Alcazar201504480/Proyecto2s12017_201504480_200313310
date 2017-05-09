package com.usacedd.estuardoarevalo.drive.api.respuestas;

import com.google.gson.annotations.SerializedName;
import com.usacedd.estuardoarevalo.drive.modelos.Archivo;
import com.usacedd.estuardoarevalo.drive.modelos.Carpeta;

import java.util.List;

/**
 * Created by estuardoarevalo on 5/7/17.
 */

public class DirectorioResponse {

    @SerializedName("error")
    public String error;

    @SerializedName("carpetas")
    public List<Carpeta> carpetas;

    @SerializedName("archivos")
    public List<Archivo> archivos;
}
