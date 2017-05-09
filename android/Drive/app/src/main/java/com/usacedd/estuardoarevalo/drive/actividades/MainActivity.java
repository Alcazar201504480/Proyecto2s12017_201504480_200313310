package com.usacedd.estuardoarevalo.drive.actividades;

import android.app.AlertDialog;
import android.app.ProgressDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.content.res.Resources;
import android.graphics.Rect;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.support.annotation.NonNull;
import android.support.design.widget.FloatingActionButton;
import android.support.v4.app.DialogFragment;
import android.support.v4.app.FragmentManager;
import android.support.v7.widget.DefaultItemAnimator;
import android.support.v7.widget.GridLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.util.TypedValue;
import android.view.View;
import android.support.design.widget.NavigationView;
import android.support.v4.view.GravityCompat;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.ArrayAdapter;
import android.widget.Toast;

import com.github.angads25.filepicker.controller.DialogSelectionListener;
import com.github.angads25.filepicker.model.DialogConfigs;
import com.github.angads25.filepicker.model.DialogProperties;
import com.github.angads25.filepicker.view.FilePickerDialog;
import com.usacedd.estuardoarevalo.drive.R;
import com.usacedd.estuardoarevalo.drive.adaptadores.CarpetaArchivo;
import com.usacedd.estuardoarevalo.drive.adaptadores.CarpetasArchivosAdapter;
import com.usacedd.estuardoarevalo.drive.api.ApiUrls;
import com.usacedd.estuardoarevalo.drive.api.DjangoApi;
import com.usacedd.estuardoarevalo.drive.api.respuestas.ComunResponse;
import com.usacedd.estuardoarevalo.drive.api.respuestas.DirectorioResponse;
import com.usacedd.estuardoarevalo.drive.dialogos.CambiarNombreCarpetaDialog;
import com.usacedd.estuardoarevalo.drive.modelos.Archivo;
import com.usacedd.estuardoarevalo.drive.modelos.Carpeta;
import com.usacedd.estuardoarevalo.drive.modelos.SesionUsuario;
import com.usacedd.estuardoarevalo.drive.utilidades.Preferencias;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;

import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.OkHttpClient;
import okhttp3.RequestBody;
import okhttp3.ResponseBody;
import okhttp3.logging.HttpLoggingInterceptor;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class MainActivity extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener,
        CambiarNombreCarpetaDialog.NoticeDialogListener,
        CarpetasArchivosAdapter.CarpetasArchivosAdapterListener{

    private RecyclerView recyclerView;
    private CarpetasArchivosAdapter adapter;
    private List<CarpetaArchivo> carpetasArchivosList;
    private String mPath;
    private DjangoApi mDjangoApi;
    private Context mContext;
    private SesionUsuario mSesionUsuario;

    private ProgressDialog mProgressDialog;
    FragmentManager mFragmentManager = getSupportFragmentManager();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mContext = getApplicationContext();
        mSesionUsuario = Preferencias.getSesionUsuario(mContext);
        mPath = "/";


        mProgressDialog = new ProgressDialog(MainActivity.this);
        mProgressDialog.setIndeterminate(false);
        mProgressDialog.setCancelable(true);


        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                DialogFragment dialog = new CambiarNombreCarpetaDialog();
                Bundle args = new Bundle();
                args.putString(CambiarNombreCarpetaDialog.ARG_TITLE, "Crear nueva carpeta");
                args.putString(CambiarNombreCarpetaDialog.ARG_MESSAGE, "Ingrese el nombre de la nueva carpeta");
                args.putString(CambiarNombreCarpetaDialog.ARG_CARPETA, "");
                args.putInt(CambiarNombreCarpetaDialog.ARG_ACTION, 2);
                args.putInt(CambiarNombreCarpetaDialog.ARG_TIPO, 0);

                dialog.setArguments(args);
                dialog.show(mFragmentManager, "tag");

            }
        });

        FloatingActionButton fab2 = (FloatingActionButton) findViewById(R.id.fab2);
        fab2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                DialogProperties properties = new DialogProperties();
                properties.selection_mode = DialogConfigs.MULTI_MODE;
                properties.selection_type = DialogConfigs.FILE_SELECT;
                properties.root = new File(DialogConfigs.DEFAULT_DIR);
                properties.error_dir = new File(DialogConfigs.DEFAULT_DIR);
                properties.offset = new File(DialogConfigs.DEFAULT_DIR);
                properties.extensions = null;
                FilePickerDialog dialog = new FilePickerDialog(MainActivity.this,properties);
                dialog.setTitle("Select a File");
                dialog.setDialogSelectionListener(new DialogSelectionListener() {
                    @Override
                    public void onSelectedFilePaths(String[] files) {
                        //files is the array of the paths of files selected by the Application User.

                        if (files.length > 0){

                            for(int i = 0; i < files.length; i++){
                                crearArchivo(files[i]);

                            }

                        }

                    }
                });
                dialog.show();

            }
        });

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.setDrawerListener(toggle);
        toggle.syncState();

        NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);
        navigationView.setNavigationItemSelectedListener(this);


        HttpLoggingInterceptor logging = new HttpLoggingInterceptor();
        logging.setLevel(HttpLoggingInterceptor.Level.BODY);
        OkHttpClient.Builder httpClient = new OkHttpClient.Builder();
        httpClient.addInterceptor(logging);  // <-- this is the important line!

        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl(ApiUrls.djangoApi)
                .addConverterFactory(GsonConverterFactory.create())
                .client(httpClient.build())
                .build();

        mDjangoApi = retrofit.create(DjangoApi.class);


        recyclerView = (RecyclerView) findViewById(R.id.recycler_view);

        carpetasArchivosList = new ArrayList<>();
        adapter = new CarpetasArchivosAdapter(mContext, carpetasArchivosList);
        adapter.setListener(this);




        RecyclerView.LayoutManager mLayoutManager = new GridLayoutManager(this, 2);
        recyclerView.setLayoutManager(mLayoutManager);
        recyclerView.addItemDecoration(new GridSpacingItemDecoration(2, dpToPx(10), true));
        recyclerView.setItemAnimator(new DefaultItemAnimator());
        recyclerView.setAdapter(adapter);

        prepararCarpetasArchivos();

    }

    @Override
    public void onBackPressed() {
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        if (drawer.isDrawerOpen(GravityCompat.START)) {
            drawer.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }else  if (id == R.id.action_subir_nivel){
            if (mPath!="/"){
                //Uri.Builder(mPath);
                Uri myUri = Uri.parse(mPath);
                mPath = "/";
                for(int i = 0; i < myUri.getPathSegments().size() - 1; i++){
                    mPath += myUri.getPathSegments().get(i) + "/";
                }
                prepararCarpetasArchivos();
            }
        }


        return super.onOptionsItemSelected(item);
    }

    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();

        if (id == R.id.nav_camera) {
            // Handle the camera action
        } else if (id == R.id.nav_gallery) {

        } else if (id == R.id.nav_slideshow) {

        } else if (id == R.id.nav_manage) {

        } else if (id == R.id.nav_share) {

        } else if (id == R.id.nav_send) {

        }

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        drawer.closeDrawer(GravityCompat.START);
        return true;
    }

    /**
     * Adding few albums for testing
     */
    private void prepararCarpetasArchivos() {


        Call<DirectorioResponse> call =
                mDjangoApi.directorio(
                        mSesionUsuario.usuario,
                        mSesionUsuario.password,
                        mPath
                );
        call.enqueue(new Callback<DirectorioResponse>() {
            @Override
            public void onResponse(Call<DirectorioResponse> call, Response<DirectorioResponse> response) {
                DirectorioResponse rsp = response.body();
                carpetasArchivosList.clear();
                if (rsp == null) {
                    Toast.makeText(mContext, "Error Django", Toast.LENGTH_SHORT).show();
                    return;
                }
                if (rsp.error == null) {
                    if(rsp.carpetas != null) {
                        CarpetaArchivo ca;
                        for (Carpeta c : rsp.carpetas) {
                            ca = new CarpetaArchivo(c.nombre, 13, R.drawable.carpeta, 0);
                            carpetasArchivosList.add(ca);

                        }
                    }
                    if(rsp.archivos != null) {
                        CarpetaArchivo ca;
                        for (Archivo a : rsp.archivos) {
                            ca = new CarpetaArchivo(a.nombre, 13, R.drawable.archivo, 1);
                            carpetasArchivosList.add(ca);

                        }
                    }
                    adapter.notifyDataSetChanged();
                }else {
                    carpetasArchivosList.clear();
                    adapter.notifyDataSetChanged();
                    Toast.makeText(mContext, rsp.error, Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<DirectorioResponse> call, Throwable t) {
                carpetasArchivosList.clear();
                adapter.notifyDataSetChanged();
                Toast.makeText(mContext, "Error al obtener el directorio \n" + t.getMessage(), Toast.LENGTH_SHORT).show();
            }
        });

    }

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        Toast.makeText(mContext, "Activity Result \n", Toast.LENGTH_SHORT).show();
    }

    @Override
    public void onDialogPositiveClick(DialogFragment dialog, int action, int tipo, String carpetaArchivo, final String inputText) {

        if (action==0) { //editar

            if (tipo==0) {

                Call<ComunResponse> call
                        = mDjangoApi.renombrar_carpeta(
                        mSesionUsuario.usuario,
                        mSesionUsuario.password,
                        mPath,
                        carpetaArchivo,
                        inputText
                );

                call.enqueue(new Callback<ComunResponse>() {
                    @Override
                    public void onResponse(Call<ComunResponse> call, Response<ComunResponse> response) {
                        ComunResponse rsp = response.body();
                        if (rsp == null) {
                            Toast.makeText(mContext, "Error Django", Toast.LENGTH_SHORT).show();
                            return;
                        }
                        if (rsp.error == null) {
                            Toast.makeText(mContext, "Nombre Cambiado correctamente.", Toast.LENGTH_SHORT).show();
                            prepararCarpetasArchivos();
                        } else {
                            Toast.makeText(mContext, rsp.error, Toast.LENGTH_SHORT).show();
                        }
                    }

                    @Override
                    public void onFailure(Call<ComunResponse> call, Throwable t) {
                        Toast.makeText(mContext, "Error al cambiar nombre de la carpeta " + inputText + ".\n" + t.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                });
            }else {

                Call<ComunResponse> call
                        = mDjangoApi.renombrar_archivo(
                        mSesionUsuario.usuario,
                        mSesionUsuario.password,
                        mPath,
                        carpetaArchivo,
                        inputText
                );

                call.enqueue(new Callback<ComunResponse>() {
                    @Override
                    public void onResponse(Call<ComunResponse> call, Response<ComunResponse> response) {
                        ComunResponse rsp = response.body();
                        if (rsp == null) {
                            Toast.makeText(mContext, "Error Django", Toast.LENGTH_SHORT).show();
                            return;
                        }
                        if (rsp.error == null) {
                            Toast.makeText(mContext, "Nombre Cambiado correctamente.", Toast.LENGTH_SHORT).show();
                            prepararCarpetasArchivos();
                        }else {
                            Toast.makeText(mContext, rsp.error, Toast.LENGTH_SHORT).show();
                        }
                    }

                    @Override
                    public void onFailure(Call<ComunResponse> call, Throwable t) {
                        Toast.makeText(mContext, "Error al cambiar nombre del archivo " + inputText + ".\n" + t.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                });
            }


        }else { //crear

            if (tipo==0) {
                Call<ComunResponse> call
                        = mDjangoApi.crear_carpeta(
                        mSesionUsuario.usuario,
                        mSesionUsuario.password,
                        mPath,
                        inputText
                );

                call.enqueue(new Callback<ComunResponse>() {
                    @Override
                    public void onResponse(Call<ComunResponse> call, Response<ComunResponse> response) {

                        ComunResponse rsp = response.body();
                        if (rsp == null) {
                            Toast.makeText(mContext, "Error Django", Toast.LENGTH_SHORT).show();
                            return;
                        }
                        if (rsp.error == null) {
                            Toast.makeText(mContext, "Carpeta creada correctamente.", Toast.LENGTH_SHORT).show();
                            prepararCarpetasArchivos();
                        } else {
                            Toast.makeText(mContext, rsp.error, Toast.LENGTH_SHORT).show();
                        }
                    }

                    @Override
                    public void onFailure(Call<ComunResponse> call, Throwable t) {
                        Toast.makeText(mContext, "Error al crear la carpeta " + inputText + ".\n" + t.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                });
            }else {
                Toast.makeText(mContext, "Abrir ventana para subir archivo", Toast.LENGTH_SHORT).show();
            }
        }
    }

    @Override
    public void onDialogNegativeClick(DialogFragment dialog) {
        //Toast.makeText(mContext, "Respuesta del dialogo Cancelado \n", Toast.LENGTH_SHORT).show();
    }

    @Override
    public void onMenuClick(String inputText, final int tipo) {


        AlertDialog.Builder builderSingle = new AlertDialog.Builder(this);
        builderSingle.setTitle("Opciones");
        final ArrayAdapter<String> arrayAdapter = new ArrayAdapter<>(this,
                android.R.layout.simple_list_item_1);

            arrayAdapter.add("Cambiar Nombre");
            arrayAdapter.add("Eliminar");

            final String nombreCarpetaArchivo = inputText;

            builderSingle.setNegativeButton("cancel",
                new DialogInterface.OnClickListener() {

                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        dialog.dismiss();
                    }
                });

            builderSingle.setAdapter(arrayAdapter,
                new DialogInterface.OnClickListener() {

                    @Override
                    public void onClick(DialogInterface dialog, int which) {

                        //Toast.makeText(getApplicationContext(),
                        //        "Opciones para \n" + nombreCarpeta ,
                        //        Toast.LENGTH_LONG).show();

                        if (which==0) {

                            //preguntar por el nuevo nombre de la carpeta o el archivo
                            if (tipo==0) {

                                DialogFragment dialogEdit = new CambiarNombreCarpetaDialog();
                                Bundle args = new Bundle();
                                args.putString(CambiarNombreCarpetaDialog.ARG_TITLE, "Cambiar nombre");
                                args.putString(CambiarNombreCarpetaDialog.ARG_MESSAGE, "Ingrese el nuevo nombre de la carpeta");
                                args.putString(CambiarNombreCarpetaDialog.ARG_CARPETA, nombreCarpetaArchivo);
                                args.putInt(CambiarNombreCarpetaDialog.ARG_ACTION, 0);
                                args.putInt(CambiarNombreCarpetaDialog.ARG_TIPO, 0);
                                dialogEdit.setArguments(args);
                                dialogEdit.show(mFragmentManager, "tag");

                            }else {
                                DialogFragment dialogEdit = new CambiarNombreCarpetaDialog();
                                Bundle args = new Bundle();
                                args.putString(CambiarNombreCarpetaDialog.ARG_TITLE, "Cambiar nombre");
                                args.putString(CambiarNombreCarpetaDialog.ARG_MESSAGE, "Ingrese el nuevo nombre del archivo");
                                args.putString(CambiarNombreCarpetaDialog.ARG_CARPETA, nombreCarpetaArchivo);
                                args.putInt(CambiarNombreCarpetaDialog.ARG_ACTION, 0);
                                args.putInt(CambiarNombreCarpetaDialog.ARG_TIPO, 1);
                                dialogEdit.setArguments(args);
                                dialogEdit.show(mFragmentManager, "tag");

                            }
                        }else {
                            if (tipo==0) {
                                //eliminar
                                eliminarCarpeta(nombreCarpetaArchivo);
                            }else {
                                //eliminar
                                eliminarArchivo(nombreCarpetaArchivo);
                            }


                        }


                    }
                });
        builderSingle.show();

    }

    @Override
    public void onCarpetaClick(String inputText) {

        mPath += inputText + "/";
        prepararCarpetasArchivos();

    }

    @Override
    public void onArchivoClick(final String inputText) {


        Call<ResponseBody> call = mDjangoApi.descargar_archivo(
                mSesionUsuario.usuario,
                mSesionUsuario.password,
                mPath,
                inputText
        );

        call.enqueue(new Callback<ResponseBody>() {
            @Override
            public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                if (response.isSuccessful()) {
                    Log.d("Descargar", "Ya se descargo y se esta intentando guardar en disco");

                    boolean writtenToDisk = writeResponseBodyToDisk(response.body(), inputText);

                    Toast.makeText(mContext, "Archivo " + inputText + " ha sido descargado.", Toast.LENGTH_SHORT).show();


                } else {
                    Toast.makeText(mContext, "Error al descargar " + inputText, Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<ResponseBody> call, Throwable t) {

            }
        });

    }



    private boolean writeResponseBodyToDisk(ResponseBody body, String nombreArchivo) {
        try {
            // todo change the file location/name according to your needs
            File futureStudioIconFile = new File(obtenerFolderDescargas() + File.separator + nombreArchivo);
            Log.d("Descargar", futureStudioIconFile.getAbsolutePath());
            InputStream inputStream = null;
            OutputStream outputStream = null;

            try {
                byte[] fileReader = new byte[4096];

                long fileSize = body.contentLength();
                long fileSizeDownloaded = 0;

                inputStream = body.byteStream();
                outputStream = new FileOutputStream(futureStudioIconFile);

                while (true) {
                    int read = inputStream.read(fileReader);

                    if (read == -1) {
                        break;
                    }

                    outputStream.write(fileReader, 0, read);

                    fileSizeDownloaded += read;

                    Log.d("Descargar", "file download: " + fileSizeDownloaded + " of " + fileSize);
                }

                outputStream.flush();

                return true;
            } catch (IOException e) {
                return false;
            } finally {
                if (inputStream != null) {
                    inputStream.close();
                }

                if (outputStream != null) {
                    outputStream.close();
                }
            }
        } catch (IOException e) {
            return false;
        }
    }


    public String obtenerFolderDescargas(){

        String path = "";
        //if there is no SD card, create new directory objects to make directory on device
        if (Environment.getExternalStorageState() == null) {
            //create new file directory object
            File directory = new File(Environment.getDataDirectory()
                    + "/DriveEDD/");

            // if no directory exists, create new directory
            if (!directory.exists()) {
                directory.mkdir();
            }

            path = directory.getAbsolutePath();

            // if phone DOES have sd card
        } else if (Environment.getExternalStorageState() != null) {
            // search for directory on SD card
            File directory = new File(Environment.getExternalStorageDirectory()
                    + "/DriveEDD/");

            // if no directory exists, create new directory to store test
            // results
            if (!directory.exists()) {
                directory.mkdir();
            }

            path = directory.getAbsolutePath();
        }// end of SD card checking

        return  path;

    }

    public void eliminarCarpeta(final String nombreCarpeta){

        Call<ComunResponse> call
                = mDjangoApi.eliminar_carpeta(
                mSesionUsuario.usuario,
                mSesionUsuario.password,
                mPath,
                nombreCarpeta
        );

        call.enqueue(new Callback<ComunResponse>() {
            @Override
            public void onResponse(Call<ComunResponse> call, Response<ComunResponse> response) {
                ComunResponse rsp = response.body();
                if (rsp == null) {
                    Toast.makeText(mContext, "Error Django", Toast.LENGTH_SHORT).show();
                    return;
                }
                if (rsp.error == null) {
                    Toast.makeText(mContext, "Carpeta eliminada correctamente.", Toast.LENGTH_SHORT).show();
                    prepararCarpetasArchivos();
                }else {
                    Toast.makeText(mContext, rsp.error, Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<ComunResponse> call, Throwable t) {
                Toast.makeText(mContext, "Error al eliminar la carpeta " + nombreCarpeta + ".\n" + t.getMessage(), Toast.LENGTH_SHORT).show();
            }
        });

    }


    public void crearArchivo(final String pathArchivo){


        mProgressDialog.setMessage("Cargando...");
        mProgressDialog.setTitle("Subiendo Archivos");
        mProgressDialog.show();



        File file = new File(pathArchivo);
        final String nombreArchivo = file.getName();

        // create RequestBody instance from file
        RequestBody requestFile =
                RequestBody.create(
                        MediaType.parse("multipart/form-data"),
                        file
                );

        // MultipartBody.Part is used to send also the actual file name
        MultipartBody.Part body =
                MultipartBody.Part.createFormData("filed", file.getName(), requestFile);

        // add another part within the multipart request
        RequestBody usuario =
                RequestBody.create(
                        okhttp3.MultipartBody.FORM, mSesionUsuario.usuario);
        RequestBody password =
                RequestBody.create(
                        okhttp3.MultipartBody.FORM, mSesionUsuario.password);
        RequestBody path =
                RequestBody.create(
                        okhttp3.MultipartBody.FORM, mPath);
        RequestBody nombre =
                RequestBody.create(
                        okhttp3.MultipartBody.FORM, nombreArchivo);


        Call<ComunResponse> call
                = mDjangoApi.crear_archivo("attachment; filename="+nombreArchivo,
                usuario, password, path, nombre, body
        );

        call.enqueue(new Callback<ComunResponse>() {
            @Override
            public void onResponse(Call<ComunResponse> call, Response<ComunResponse> response) {
                mProgressDialog.dismiss();
                ComunResponse rsp = response.body();
                if (rsp == null) {
                    Toast.makeText(mContext, "Error Django", Toast.LENGTH_SHORT).show();
                    return;
                }
                if (rsp.error == null) {
                    Toast.makeText(mContext, "Archivo Creado correctamente.", Toast.LENGTH_SHORT).show();
                    prepararCarpetasArchivos();
                }else {
                    Toast.makeText(mContext, rsp.error, Toast.LENGTH_SHORT).show();
                }


            }

            @Override
            public void onFailure(Call<ComunResponse> call, Throwable t) {
                Toast.makeText(mContext, "Error al crear el archivo " + nombreArchivo + ".\n" + t.getMessage(), Toast.LENGTH_SHORT).show();
                mProgressDialog.dismiss();
            }
        });

    }



    public void eliminarArchivo(final String nombreArchivo){

        Call<ComunResponse> call
                = mDjangoApi.eliminar_archivo(
                mSesionUsuario.usuario,
                mSesionUsuario.password,
                mPath,
                nombreArchivo
        );

        call.enqueue(new Callback<ComunResponse>() {
            @Override
            public void onResponse(Call<ComunResponse> call, Response<ComunResponse> response) {
                ComunResponse rsp = response.body();
                if (rsp == null) {
                    Toast.makeText(mContext, "Error Django", Toast.LENGTH_SHORT).show();
                    return;
                }
                if (rsp.error == null) {
                    Toast.makeText(mContext, "Archivo eliminado correctamente.", Toast.LENGTH_SHORT).show();
                    prepararCarpetasArchivos();
                }else {
                    Toast.makeText(mContext, rsp.error, Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<ComunResponse> call, Throwable t) {
                Toast.makeText(mContext, "Error al eliminar el archivo " + nombreArchivo + ".\n" + t.getMessage(), Toast.LENGTH_SHORT).show();
            }
        });

    }


    /**
     * RecyclerView item decoration - give equal margin around grid item
     */
    public class GridSpacingItemDecoration extends RecyclerView.ItemDecoration {

        private int spanCount;
        private int spacing;
        private boolean includeEdge;

        public GridSpacingItemDecoration(int spanCount, int spacing, boolean includeEdge) {
            this.spanCount = spanCount;
            this.spacing = spacing;
            this.includeEdge = includeEdge;
        }

        @Override
        public void getItemOffsets(Rect outRect, View view, RecyclerView parent, RecyclerView.State state) {
            int position = parent.getChildAdapterPosition(view); // item position
            int column = position % spanCount; // item column

            if (includeEdge) {
                outRect.left = spacing - column * spacing / spanCount; // spacing - column * ((1f / spanCount) * spacing)
                outRect.right = (column + 1) * spacing / spanCount; // (column + 1) * ((1f / spanCount) * spacing)

                if (position < spanCount) { // top edge
                    outRect.top = spacing;
                }
                outRect.bottom = spacing; // item bottom
            } else {
                outRect.left = column * spacing / spanCount; // column * ((1f / spanCount) * spacing)
                outRect.right = spacing - (column + 1) * spacing / spanCount; // spacing - (column + 1) * ((1f /    spanCount) * spacing)
                if (position >= spanCount) {
                    outRect.top = spacing; // item top
                }
            }
        }
    }

    /**
     * Converting dp to pixel
     */
    private int dpToPx(int dp) {
        Resources r = getResources();
        return Math.round(TypedValue.applyDimension(TypedValue.COMPLEX_UNIT_DIP, dp, r.getDisplayMetrics()));
    }


}


