import android.content.Intent;
// ... imports

public class MainActivity extends AppCompatActivity {
    // ... existing code

    private void startBackgroundMiner() {
        Intent serviceIntent = new Intent(this, com.frostprotocol.core.FrostMinerService.class);
        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
            startForegroundService(serviceIntent);
        } else {
            startService(serviceIntent);
        }
    }

    private void stopBackgroundMiner() {
        Intent serviceIntent = new Intent(this, com.frostprotocol.core.FrostMinerService.class);
        serviceIntent.setAction("STOP");
        startService(serviceIntent);
    }
    
    // Call these methods inside your Button listeners, e.g.:
    // findViewById(R.id.btnStartMining).setOnClickListener(v -> startBackgroundMiner());
}
