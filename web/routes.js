var dbManager = require('./functions/dbManager');

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


router.get('/sql/account_univserse', (req, res) => {

  //TODO: this
});



router.get('/*', (req, res) => {
    var q = url.parse(req.url, true);
    var filename =  q.pathname;

    if(filename == "/"){
      filename = "/library.html";
    }
    fileReader.fileReader(filename,req,res);
});

module.exports = router;
