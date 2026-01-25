// Eric's Games: UI Core Module 2026
const EricsGamesDashboard = () => {
  return (
    <div className="min-h-screen bg-[#020617] text-[#22d3ee] p-8"> 
      {/* Precision (Virgo Influence) Header */}
      <div className="backdrop-blur-xl bg-white/5 border border-white/10 p-6 rounded-3xl shadow-2xl">
        <h1 className="text-3xl font-black tracking-tighter">ERIC'S GAMES | NEURAL NEXUS</h1>
        <div className="flex gap-4 mt-4">
          <div className="px-3 py-1 bg-cyan-900/30 rounded-full text-[10px] border border-cyan-500/50">100.00% SYNC</div>
          <div className="px-3 py-1 bg-purple-900/30 rounded-full text-[10px] border border-purple-500/50">FROSTCHAIN ACTIVE</div>
        </div>
      </div>

      {/* Game Modules */}
      <div className="grid grid-cols-2 gap-6 mt-8">
        <div className="p-8 bg-white/5 rounded-3xl border border-white/5 hover:border-cyan-400 transition-all cursor-pointer">
          <h2 className="text-xl font-bold">Sphynx Slots v3</h2>
          <p className="text-xs text-slate-400 mt-2">Provably Fair | Multi-Asset Bridge</p>
        </div>
        <div className="p-8 bg-white/5 rounded-3xl border border-white/5 hover:border-cyan-400 transition-all cursor-pointer">
          <h2 className="text-xl font-bold">DOGE Dice</h2>
          <p className="text-xs text-slate-400 mt-2">Velocity Pulse | Instant Settlement</p>
        </div>
      </div>
    </div>
  );
};
