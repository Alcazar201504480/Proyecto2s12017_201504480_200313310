package com.usacedd.estuardoarevalo.drive.api.respuestas;

import com.google.gson.annotations.SerializedName;

/**
 * Created by estuardoarevalo on 3/28/17.
 *
 *
 {
 "nombre": "Estuardo",
 "apellido": "Arevalo",
 "email": "earevalo",
 "contra": "earevalo",
 "naci": "nop"
 }
 */

public class IniciarSesionResponse {

    @SerializedName("nombre")
    public String nombre;

    @SerializedName("apellido")
    public String apellido;

    @SerializedName("email")
    public String usuario;

    @SerializedName("contra")
    public String password;

    @SerializedName("naci")
    public String nacimiento;

    @SerializedName("error")
    public String error;

}
