package com.usacedd.estuardoarevalo.drive.api;

import com.usacedd.estuardoarevalo.drive.api.respuestas.ComunResponse;
import com.usacedd.estuardoarevalo.drive.api.respuestas.DirectorioResponse;
import com.usacedd.estuardoarevalo.drive.api.respuestas.IniciarSesionResponse;

import okhttp3.MultipartBody;
import okhttp3.RequestBody;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.Header;
import retrofit2.http.Multipart;
import retrofit2.http.POST;
import retrofit2.http.PUT;
import retrofit2.http.Part;

/**
 * Created by estuardoarevalo on 3/28/17.
 */

public interface DjangoApi {

    @FormUrlEncoded
    @POST("login/")
    Call<IniciarSesionResponse> iniciarSesion(@Field("usuario") String usuario,
                                              @Field("password") String contrasena);

    @FormUrlEncoded
    @POST("directorio_usuario/")
    Call<DirectorioResponse> directorio(@Field("usuario") String usuario,
                                                @Field("password") String contrasena,
                                                @Field("path") String path);

    @FormUrlEncoded
    @POST("crear_carpeta_usuario/")
    Call<ComunResponse> crear_carpeta(@Field("usuario") String usuario,
                                      @Field("password") String contrasena,
                                      @Field("path") String path,
                                      @Field("nombreCarpeta") String nombreCarpeta);

    @FormUrlEncoded
    @POST("renombrar_carpeta_usuario/")
    Call<ComunResponse> renombrar_carpeta(@Field("usuario") String usuario,
                                          @Field("password") String contrasena,
                                          @Field("path") String path,
                                          @Field("nombreCarpeta") String nombreCarpeta,
                                          @Field("nuevoNombre") String nuevoNombre);

    @FormUrlEncoded
    @POST("eliminar_carpeta_usuario/")
    Call<ComunResponse> eliminar_carpeta(@Field("usuario") String usuario,
                                      @Field("password") String contrasena,
                                      @Field("path") String path,
                                      @Field("nombreArchivo") String nombreArchivo);

    @Multipart
    @PUT("crear_archivo_usuario/")
    Call<ComunResponse> crear_archivo(@Header("Content-Disposition") String header,
                                      @Part("usuario") RequestBody usuario,
                                      @Part("password") RequestBody contrasena,
                                      @Part("path") RequestBody path,
                                      @Part("nombreArchivo") RequestBody nombreArchivo,
                                      @Part MultipartBody.Part file);

    @FormUrlEncoded
    @POST("renombrar_archivo_usuario/")
    Call<ComunResponse> renombrar_archivo(@Field("usuario") String usuario,
                                          @Field("password") String contrasena,
                                          @Field("path") String path,
                                          @Field("nombreArchivo") String nombreArchivo,
                                          @Field("nuevoNombre") String nuevoNombre);

    @FormUrlEncoded
    @POST("eliminar_archivo_usuario/")
    Call<ComunResponse> eliminar_archivo(@Field("usuario") String usuario,
                                         @Field("password") String contrasena,
                                         @Field("path") String path,
                                         @Field("nombreArchivo") String nombreArchivo);

    @FormUrlEncoded
    @POST("descargar_archivo_usuario/")
    Call<ResponseBody> descargar_archivo(@Field("usuario") String usuario,
                                         @Field("password") String contrasena,
                                         @Field("path") String path,
                                         @Field("nombreArchivo") String nombreArchivo);
}
