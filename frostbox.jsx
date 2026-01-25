// Frost OS: FrostBox Kernel Module
const FrostBoxStorage = () => {
  return (
    <div className="p-4 bg-white/5 rounded-2xl border border-cyan-500/20 backdrop-blur-xl">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-sm font-bold tracking-tighter text-cyan-400">🖇️ FROSTBOX ARCHIVE</h2>
        <span className="text-[10px] text-slate-500">100% SYNCED</span>
      </div>
      {/* Visualizing the "1 to 0" Settlement */}
      <div className="w-full h-2 bg-slate-900 rounded-full overflow-hidden">
        <div className="h-full bg-cyan-500 w-[100%] animate-pulse"></div>
      </div>
      <p className="text-[10px] mt-2 text-slate-400 font-mono">ENCRYPTED KEY: ALPHA_WINTER_GHOST</p>
    </div>
  );
};
