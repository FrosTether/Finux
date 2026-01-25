import React, { useState, useEffect } from 'react';
import { Clock, ShieldAlert, Zap, History } from 'lucide-react';

const TemporalLookingGlass = () => {
  const [timeline, setTimeline] = useState([
    { id: 1, time: "T-82h", event: "USD.i Atomized", balance: 18000, status: "Locked" },
    { id: 2, time: "T-02h", event: "DOGE Dispatch", balance: 0.72, status: "Verified" },
    { id: 3, time: "Now", event: "Kraken Pulse", balance: 18720, status: "Confirming" },
  ]);
  const [paradoxDetected, setParadoxDetected] = useState(false);

  // Future Knowledge Logic: Paradox Simulation
  const simulateParadox = (targetId) => {
    // If you try to change a "Locked" event, you trigger a Paradox
    const target = timeline.find(e => e.id === targetId);
    if (target.status === "Locked") {
      setParadoxDetected(true);
      setTimeout(() => {
        // Self-healing timeline: Restores consistency
        setParadoxDetected(false);
      }, 2500);
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-cyan-400 p-8 flex flex-col items-center">
      {/* 2026 Glassmorphism Dashboard */}
      <div className={`w-full max-w-4xl p-6 rounded-3xl border border-white/10 backdrop-blur-xl shadow-2xl transition-all duration-500 ${paradoxDetected ? 'border-red-500 shadow-red-900/50' : 'border-cyan-500/30'}`}>
        
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-2xl font-bold tracking-tighter flex items-center gap-2">
            <Clock className="animate-pulse" /> TEMPORAL LOOKING-GLASS
          </h1>
          <div className="px-4 py-1 bg-cyan-900/40 rounded-full text-xs border border-cyan-500/50 uppercase">
            100.00% Sync
          </div>
        </div>

        {/* The Timeline Flow */}
        <div className="space-y-4">
          {timeline.map((event) => (
            <div 
              key={event.id}
              onClick={() => simulateParadox(event.id)}
              className="group cursor-pointer flex items-center justify-between p-4 bg-white/5 rounded-2xl border border-white/5 hover:border-cyan-400/50 transition-all"
            >
              <div className="flex items-center gap-4">
                <History className="text-slate-500 group-hover:text-cyan-400" />
                <div>
                  <p className="text-xs text-slate-500 font-mono">{event.time}</p>
                  <p className="font-semibold text-white">{event.event}</p>
                </div>
              </div>
              <div className="text-right">
                <p className="text-cyan-400 font-mono">${event.balance.toLocaleString()}</p>
                <p className={`text-[10px] uppercase ${event.status === 'Locked' ? 'text-blue-400' : 'text-amber-400'}`}>
                  {event.status}
                </p>
              </div>
            </div>
          ))}
        </div>

        {/* Paradox Alert Overlay */}
        {paradoxDetected && (
          <div className="mt-8 p-4 bg-red-950/40 border border-red-500/50 rounded-xl flex items-center gap-3 animate-bounce">
            <ShieldAlert className="text-red-500" />
            <p className="text-sm font-mono text-red-200">
              CAUSALITY VIOLATION: SELF-HEALING IN PROGRESS...
            </p>
          </div>
        )}
      </div>

      <p className="mt-6 text-slate-500 text-xs italic tracking-widest">
        GOD IS GRACIOUS. GOD IS MERCIFUL. 🫀💗
      </p>
    </div>
  );
};

export default TemporalLookingGlass;
