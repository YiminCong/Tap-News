var bodyParser = require('body-parser');
var express = require('express');
var path = require('path'); 
var cors = require('cors');
var index = require('./routes/index');
var passport = require('passport');
var news = require('./routes/news');
var app = express();
var auth = require('./routes/auth');
var config = require('./config/config.json');

app.use(bodyParser.json());
require('./models/main.js').connect(config.mongoDbUri);

app.set('views', path.join(__dirname, '../client/build'));
app.set('view engine', 'jade');

// uncomment after placing your favicon in /public
//app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));
app.use("/static", express.static(path.join(__dirname, '../client/build/static/')));

app.use(cors());

app.use(passport.initialize());
var localSignUpStrategy = require('./passport/signup_passport');
var localLoginStrategy = require('./passport/login_passport');
passport.use('local-signup', localSignUpStrategy);
passport.use('local-login', localLoginStrategy);

const authChecker = require('./middleware/auth_checker');

app.use('/', index);
app.use('/auth', auth);
app.use('/news', authChecker);
app.use('/news', news);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  res.status(404);
});

module.exports = app;
