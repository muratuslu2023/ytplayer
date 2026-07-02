document.getElementById('musicForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const url = document.getElementById('urlInput').value;
        const audioPlayer = document.getElementById('audioPlayer');
        const playerSection = document.getElementById('playerSection');

        const response = await fetch('/process-music', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ music_url: url }),
        });

        const result = await response.json();

        if (result.playable_url) {
            // Set the audio source and reveal the player
            audioPlayer.src = result.playable_url;
            playerSection.classList.remove('hidden');
            audioPlayer.play();
        } else {
            alert('Could not retrieve audio.');
        }
    });


