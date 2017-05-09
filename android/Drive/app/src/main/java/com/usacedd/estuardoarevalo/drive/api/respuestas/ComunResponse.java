package com.usacedd.estuardoarevalo.drive.api.respuestas;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

/**
 * Created by estuardoarevalo on 3/29/17.
 */

public class ComunResponse {
    @SerializedName("success")
    @Expose
    public int success;

    @SerializedName("error")
    public String error;


}
