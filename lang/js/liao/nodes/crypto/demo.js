const 
  fs = require('fs'),
  crypto = require('crypto');

function loadKey(file) {
  return fs.readFileSync(file, 'utf8');
}

let 
  prvKey = loadKey('./rsa-prv.pem'),
  pubKey = loadKey('./rsa-pub.pem'),
  message = 'Hello NodeJS !';

// 私钥加密，公钥解密
let enc_by_prv = crypto.privateEncrypt(prvKey, Buffer.from(message, 'utf-8'));
console.log('encrypted by private key: ' + enc_by_prv.toString('hex'));
let dec_by_pub = crypto.publicDecrypt(pubKey, enc_by_prv);
console.log('decrypted by public key: ' + dec_by_pub.toString('utf8'));

console.log('----------------------------------------------')


// 公钥加密，私钥解密
let enc_by_pub = crypto.publicEncrypt(pubKey, Buffer.from(message, 'utf-8'));
console.log('encrypted by public key: ' + enc_by_pub.toString('hex'));
let dec_by_pri = crypto.privateDecrypt(prvKey, enc_by_pub);
console.log('decrypted by private key: ' + dec_by_pub.toString('utf8'));
