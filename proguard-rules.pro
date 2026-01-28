# --- FROST PROTOCOL: SECURITY & SHRINKAGE ---

# 1. Aggressive Overload Induction (Shrinks code size)
-optimizationpasses 5
-allowaccessmodification
-mergeinterfacesaggressively

# 2. Protect the Core Kernel (Don't rename your main scripts)
-keep class com.frost.protocol.CoreKernel { *; }
-keep class com.frost.optimizer.** { *; }

# 3. Strip Logs for Production (Speed boost)
-assumenosideeffects class android.util.Log {
    public static boolean isLoggable(java.lang.String, int);
    public static int v(...);
    public static int d(...);
    public static int i(...);
    public static int w(...);
}

# 4. Google Play Services Optimization
-keep public class com.google.android.gms.* { public *; }
