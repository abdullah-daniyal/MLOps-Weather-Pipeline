const express = require('express');
const mongoose = require('mongoose');
const dotenv = require('dotenv');
const cors = require('cors');
const path = require('path');

// Load environment variables
dotenv.config();

const app = express();

// Middleware
app.use(express.json());
app.use(cors());

// Connect to MongoDB
mongoose
    .connect(process.env.MONGODB_URI, {
        useNewUrlParser: true,
        useUnifiedTopology: true,
    })
    .then(() => console.log('MongoDB Connected'))
    .catch((err) => {
        console.error(err.message);
        process.exit(1);
    });

// Define Routes
app.use('/api/auth', require('./routes/authRoutes'));
app.use('/api/predict', require('./routes/predictRoutes'));

// Serve Frontend (optional, to be configured later)
// app.use(express.static(path.join(__dirname, '../frontend/dist')));

// Define the port
const PORT = process.env.PORT || 5000;

app.listen(PORT, () => console.log(`Server started on port ${PORT}`));
