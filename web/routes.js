var dbManager = require('./functions/dbManager');
var fileReader = require('./functions/fileReader');
var url = require('url');
var express = require('express');
var router = express.Router();
router.use(express.static('public'));

router.get('/add/universe', (req, res) => {
  var name = req.query.name;
  console.log("adding universe: ");
  console.log(req.query);
  res.json({result:dbManager.addUniverse(name)});
});

router.get('/add/language', (req, res) => {
  var name = req.query.name;
  var id = req.query.universe_id;
  console.log("adding language: ");
  console.log(req.query);
  res.json({result:dbManager.addLanguage(name, id)});
});
router.get('/add/word', (req, res) => {
  var word = req.query.word;
  var id = req.query.language_id;
  console.log("adding word: ");
  console.log(req.query);
  res.json({result:dbManager.addWord(word, id)});
});
router.get('/add/definition', (req, res) => {
  var def = req.query.def;
  var id = req.query.word_id;
  var type = req.query.type;
  console.log("adding definition: ");
  console.log(req.query);
  res.json({result:dbManager.addDefinition(def, id, type)});
});



router.get('/sql/universes', (req, res) => {

     res.json(dbManager.getAllUniverses());
});

router.get('/sql/languages', (req, res) => {

    res.json(dbManager.getAllLanguages());
});

router.get('/sql/words', (req, res) => {

    res.json(dbManager.getAllWords());
});

router.get('/sql/definitions', (req, res) => {

  res.json(dbManager.getAllDefinitions());
});

router.get('/sql/dictionary', (req, res) => {
  var universe = req.query.universe;
  var language = req.query.language;
  var word = req.query.word; 
  var db = dbManager.getDB();
  db.all(`select * from (select words.id as wrd_id, word, universe_id,language_id,language_name,universe_name from (select universe_id,languages.id as lang_id,universes.name as universe_name, languages.name as language_name from universes join languages on universes.id=languages.universe_id) join words on language_id=words.language_id) left join definitions on wrd_id=definitions.word_id`,
   (err, row) => {
   if (err) {
     console.error(err.message);
   }
   console.log(row);
   res.json({dictionary: row});
  });
});


router.get('/sql/account_univserse', (req, res) => {

  //TODO: this
});




router.get('/*', (req, res) => {
    var q = url.parse(req.url, true);
    var filename =  q.pathname;
    filename = "/home.html";
    fileReader.fileReader(filename,req,res);
});

module.exports = router;
