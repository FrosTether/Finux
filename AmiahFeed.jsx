// Connects to your Monroeville Node API
function AmiahFeed() {
  const [doodles, setDoodles] = useState([]);

  const handleTap = (permlink) => {
    // Triggers the 'tap_it_out' python function via API
    api.post('/tap', { permlink, weight: 100 });
  };

  return (
    <div className="amiah-feed">
      {doodles.map(post => (
        <div className="doodle-card">
          <img src={`https://ipfs.io/ipfs/${post.ipfs_cid}`} />
          <h3>{post.caption}</h3>
          <button onClick={() => handleTap(post.permlink)}>
            👆 TAP IT OUT ({post.taps})
          </button>
        </div>
      ))}
    </div>
  );
}
