var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("test1");
    var myobj = { chapter: "Equilibrium", subject: "Physics", date: "01-01-2021", minr: 1, maxr: 6 }
    dbo.collection("tt_automatic").insertOne(myobj, function (err, res) {
        if (err) throw err;
        db.close();
    });   
});
