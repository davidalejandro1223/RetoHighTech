var albumBucketName = 'faces.demo.htsoft';
var bucketRegion = 'us-east-1';
var fotoName = 'foto5.jpg';

AWS.config.update({
  region: bucketRegion,
  credentials: new AWS.Credentials('')
});

var s3 = new AWS.S3({
  apiVersion: '2006-03-01',
  params: {Bucket: albumBucketName}
});


function uploadPhoto(blobData) {
  fotoName = 'fotoReto1.jpg';
  var albumPhotosKey = 'fotosAI/';
  var photoKey = albumPhotosKey + fotoName;
  s3.upload({
    Key: photoKey,
    Body: blobData,
    ACL: 'private'
  }, function(err, data) {
    if (err) {
      return alert('Hubo en error cargando la foto: ', err.message);
	}
	else{
    console.log(data);
	}
  });
} 


