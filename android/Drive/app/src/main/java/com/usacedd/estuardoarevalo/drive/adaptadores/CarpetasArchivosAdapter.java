package com.usacedd.estuardoarevalo.drive.adaptadores;

import android.content.ClipData;
import android.content.Context;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.bumptech.glide.Glide;
import com.usacedd.estuardoarevalo.drive.R;

import java.util.List;

/**
 *
 */
public class CarpetasArchivosAdapter extends RecyclerView.Adapter<CarpetasArchivosAdapter.MyViewHolder> {

    private Context mContext;
    private List<CarpetaArchivo> carpetaArchivoList;
    // Use this instance of the interface to deliver action events
    CarpetasArchivosAdapterListener mListener;

    public class MyViewHolder extends RecyclerView.ViewHolder {
        public TextView title, count;
        public ImageView thumbnail, overflow;
        public CarpetaArchivo currentItem;

        public MyViewHolder(View view) {
            super(view);
            title = (TextView) view.findViewById(R.id.title);
            count = (TextView) view.findViewById(R.id.count);
            thumbnail = (ImageView) view.findViewById(R.id.thumbnail);
            overflow = (ImageView) view.findViewById(R.id.overflow);

            thumbnail.setOnClickListener(new View.OnClickListener() {
                @Override public void onClick(View v) {
                    // item clicked
                    if (currentItem.getTipo() == 0)
                        mListener.onCarpetaClick(currentItem.getNombre());
                    else
                        mListener.onArchivoClick(currentItem.getNombre());
                }
            });

            view.setOnClickListener(new View.OnClickListener() {
                @Override public void onClick(View v) {
                    // item clicked
                    if (currentItem.getTipo() == 0)
                        mListener.onCarpetaClick(currentItem.getNombre());
                    else
                        mListener.onArchivoClick(currentItem.getNombre());
                }
            });
        }
    }


    public CarpetasArchivosAdapter(Context mContext, List<CarpetaArchivo> carpetaArchivoList) {
        this.mContext = mContext;
        this.carpetaArchivoList = carpetaArchivoList;
    }

    public void setListener(CarpetasArchivosAdapterListener l){
        mListener = l;
    }

    @Override
    public MyViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View itemView = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.carpetaarchivo_card, parent, false);

        return new MyViewHolder(itemView);
    }

    @Override
    public void onBindViewHolder(final MyViewHolder holder, int position) {
        final CarpetaArchivo carpetaArchivo = carpetaArchivoList.get(position);
        holder.title.setText(carpetaArchivo.getNombre());
        holder.count.setText(carpetaArchivo.getNumDeArchivos() + " archivo(s)");
        holder.currentItem = carpetaArchivo;
        final String nombreCarpetaArchivo = carpetaArchivo.getNombre();
        // loading carpetaArchivo cover using Glide library
        Glide.with(mContext).load(carpetaArchivo.getMiniatura()).into(holder.thumbnail);

        holder.overflow.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                mListener.onMenuClick(nombreCarpetaArchivo,carpetaArchivo.getTipo());

                Toast.makeText(mContext,
                        "Click en menu de " + nombreCarpetaArchivo,
                        Toast.LENGTH_LONG).show();


            }
        });
    }

    @Override
    public int getItemCount() {
        return carpetaArchivoList.size();
    }

    /* The activity that creates an instance of this dialog fragment must
     * implement this interface in order to receive event callbacks.
     * Each method passes the DialogFragment in case the host needs to query it. */
    public interface CarpetasArchivosAdapterListener {
        public void onMenuClick(String inputText, int tipo);
        public void onCarpetaClick(String inputText);
        public void onArchivoClick(String inputText);

    }
}
