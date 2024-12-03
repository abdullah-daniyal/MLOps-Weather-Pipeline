const express = require('express');
const router = express.Router();
const { predict } = require('../controllers/predictController');
const authMiddleware = require('../utils/authMiddleware');

// @route   POST /api/predict
// @desc    Get temperature prediction
// @access  Private
router.post('/', authMiddleware, predict);

module.exports = router;
