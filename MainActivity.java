import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import com.frostprotocol.core.FrostLink;

public class MainActivity extends AppCompatActivity {

    private FrostLink frostLink;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize connection to your Cloud Node
        // REPLACE WITH YOUR COMPUTER'S IP if testing on real device
        frostLink = new FrostLink("http://192.168.1.15:5000"); 

        // Connect immediately on app launch
        System.out.println("Starting Frost Protocol...");
        frostLink.performHandshake();

        // Example: Trigger a transaction when a button is clicked
        // findViewById(R.id.payButton).setOnClickListener(v -> {
        //     frostLink.sendTransaction("wallet_kelsee_mobile", 100.0);
        // });
    }
}
