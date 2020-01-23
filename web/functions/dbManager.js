const sqlite3 = require("sqlite3").verbose();


exports.getDB = function(){
  let db = new sqlite3.Database('./db/conlang.sl3',sqlite3.OPEN_READWRITE, (err) => {
    if (err) {
      return console.error(err.message);
    }
    console.log('Connected to the in-memory SQlite database.');
  });
  return db;
}


exports.addUniverse = function(name){
  var db = getDB();
  db.run(`INSERT INTO universes(name) VALUES(?)`, [name], function(err) {
    if (err) {
      return console.log(err.message);
    }
  });
  db.close();
  return "Success";
}

exports.addLanguage = function(name, universe_id){
  var db = getDB();
  db.run(`INSERT INTO languages(name,universe_id) VALUES(?,?)`, [name,universe_id], function(err) {
    if (err) {
      return console.log(err.message);
    }
  });
  db.close();
  return "Success";
}

exports.addWord = function(word, language_id){
  var db = getDB();
  db.run(`INSERT INTO words(word, language_id) VALUES(?, ?)`, [word, language_id], function(err) {
    if (err) {
      return console.log(err.message);
    }
  });
  db.close();
  return "Success";
}

exports.addDefinition = function(def, word_id, type){
  var db = getDB();
  db.run(`INSERT INTO definitions(definition, word_id, type) VALUES(?, ?, ?)`, [def, word_id, type], function(err) {
    if (err) {
      return console.log(err.message);
    }
  });
  db.close();
  return "Success";
}

exports.getAllUniverses = function(){
  var db = getDB();
  db.all(`select * from universes`,
   (err, row) => {
   if (err) {
     console.error(err.message);
   }
   result = {universes: row};
  });
  db.close();
  return result;
}

exports.getAllLanguages = function(){
  var db = getDB();
  db.all(`select * from languages`,
   (err, row) => {
   if (err) {
     console.error(err.message);
   }
   result = {languages: row};
});
  db.close();
  return result;
}

exports.getAllWords = function(){
  var db = getDB();
  db.all(`select * from words`,
   (err, row) => {
   if (err) {
     console.error(err.message);
   }
   result = {words: row};
  });
  db.close();
  return result;
}

exports.getAllDefinitions = function(){
  var db = getDB();
  db.all(`select * from definitions`,
   (err, row) => {
   if (err) {
     console.error(err.message);
   }
   result = {definitions: row};
  });
  db.close();
  return result;
}
exports.getDictionary = function(universe,language,word){
  var db = getDB();
  var results = []
  db.all(`select * from (select words.id as wrd_id, word, universe_id,language_id,language_name,universe_name from (select universe_id,languages.id as lang_id,universes.name as universe_name, languages.name as language_name from universes join languages on universes.id=languages.universe_id) join words on language_id=words.language_id) left join definitions on wrd_id=definitions.word_id`,
   (err, row) => {
   if (err) {
     console.error(err.message);
   }
   return {definitions: row};
  });
}
