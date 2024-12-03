const { spawn } = require('child_process');
const path = require('path');

exports.predict = async (req, res) => {
    const { humidity, wind_speed } = req.body;

    if (humidity === undefined || wind_speed === undefined) {
        return res.status(400).json({ message: 'Humidity and Wind Speed are required' });
    }

    try {
        const pythonProcess = spawn('python', [
            path.join(__dirname, '../python/predict.py'),
            humidity,
            wind_speed,
        ]);

        pythonProcess.stdout.on('data', (data) => {
            const prediction = data.toString();
            res.json({ predicted_temperature: parseFloat(prediction) });
        });

        pythonProcess.stderr.on('data', (data) => {
            console.error(`stderr: ${data}`);
            res.status(500).json({ message: 'Error in prediction script' });
        });

        pythonProcess.on('close', (code) => {
            if (code !== 0) {
                console.error(`Python script exited with code ${code}`);
            }
        });
    } catch (error) {
        console.error(error.message);
        res.status(500).send('Server error');
    }
};
