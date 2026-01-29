<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:background="#0D1117"
    android:padding="24dp">

    <TextView
        android:id="@+id/headerTitle"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="FROST PROTOCOL"
        android:fontFamily="monospace"
        android:textColor="#58A6FF"
        android:textSize="18sp"
        android:letterSpacing="0.1"
        android:layout_gravity="center_horizontal"
        android:layout_marginTop="20dp" />

    <androidx.cardview.widget.CardView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="30dp"
        app:cardBackgroundColor="#161B22"
        app:cardCornerRadius="12dp"
        app:cardElevation="4dp">

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:padding="24dp">

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="CURRENT BALANCE"
                android:textColor="#8B949E"
                android:textSize="12sp"
                android:fontFamily="monospace"/>

            <TextView
                android:id="@+id/tvBalance"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="0.00 FNR"
                android:textColor="#FFFFFF"
                android:textSize="32sp"
                android:textStyle="bold"
                android:layout_marginTop="8dp"/>
                
            <TextView
                android:id="@+id/tvStatus"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="● Node Synchronized"
                android:textColor="#238636"
                android:textSize="12sp"
                android:layout_marginTop="4dp"/>
        </LinearLayout>
    </androidx.cardview.widget.CardView>

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="SEND TOKENS"
        android:textColor="#8B949E"
        android:textSize="14sp"
        android:layout_marginTop="40dp"
        android:layout_marginBottom="10dp"
        android:fontFamily="monospace"/>

    <EditText
        android:id="@+id/etRecipient"
        android:layout_width="match_parent"
        android:layout_height="50dp"
        android:background="#21262D"
        android:hint="Recipient ID / Wallet Address"
        android:textColorHint="#484F58"
        android:textColor="#FFFFFF"
        android:paddingStart="16dp"
        android:inputType="textNoSuggestions"/>

    <EditText
        android:id="@+id/etAmount"
        android:layout_width="match_parent"
        android:layout_height="50dp"
        android:background="#21262D"
        android:layout_marginTop="16dp"
        android:hint="Amount (FNR)"
        android:textColorHint="#484F58"
        android:textColor="#FFFFFF"
        android:paddingStart="16dp"
        android:inputType="numberDecimal"/>

    <Button
        android:id="@+id/btnSend"
        android:layout_width="match_parent"
        android:layout_height="60dp"
        android:layout_marginTop="24dp"
        android:text="EXECUTE TRANSFER"
        android:backgroundTint="#238636"
        android:textColor="#FFFFFF"
        android:fontFamily="monospace"
        android:textSize="16sp"/>

</LinearLayout>
