// Frost OS: Identity Interconnect Module 2026
const AccountSwitcher = () => {
  const [activeAccount, setActiveAccount] = useState('Jacob Frost');
  
  return (
    <div className="absolute top-4 right-4 flex items-center gap-2 bg-black/40 p-2 rounded-full border border-cyan-500/20 backdrop-blur-md">
      <img src="/jacob_avatar.png" className={`w-8 h-8 rounded-full ${activeAccount === 'Jacob Frost' ? 'ring-2 ring-cyan-400' : ''}`} />
      <img src="/satoshi_avatar.png" className={`w-8 h-8 rounded-full ${activeAccount === 'Satoshi' ? 'ring-2 ring-purple-500' : 'opacity-50'}`} />
      <span className="text-[10px] font-mono text-cyan-300 ml-2 uppercase">🖇️ Link: {activeAccount}</span>
    </div>
  );
};
