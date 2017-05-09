package com.usacedd.estuardoarevalo.drive.adaptadores;

/**
 * Created by Lincoln on 18/05/16.
 */
public class CarpetaArchivo {
    private String nombre;
    private int numDeArchivos;
    private int miniatura;
    private int tipo;

    public CarpetaArchivo() {
    }

    public CarpetaArchivo(String nombre, int numDeArchivos, int miniatura, int tipo) {
        this.nombre = nombre;
        this.numDeArchivos = numDeArchivos;
        this.miniatura = miniatura;
        this.setTipo(tipo);
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getNumDeArchivos() {
        return numDeArchivos;
    }

    public void setNumDeArchivos(int numDeArchivos) {
        this.numDeArchivos = numDeArchivos;
    }

    public int getMiniatura() {
        return miniatura;
    }

    public void setMiniatura(int miniatura) {
        this.miniatura = miniatura;
    }

    public int getTipo() {
        return tipo;
    }

    public void setTipo(int tipo) {
        this.tipo = tipo;
    }
}
