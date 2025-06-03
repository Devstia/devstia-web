String.prototype.delRightMost=function(sFind){
  for (var i = this.length; i >= 0; i = i - 1) {
    var f = this.indexOf(sFind, i);
    if (f != -1) {
       return this.substr(0, f);
       break;
    }
  }
  return this;
};
String.prototype.getRightMost=function(sFind){
  for (var i = this.length; i >= 0; i = i - 1) {
    var f = this.indexOf(sFind, i);
    if (f != -1) {
       return this.substr(f + sFind.length, this.length);
    }
  }
  return this;
};
String.prototype.delLeftMost=function(sFind){
  for (var i = 0; i < this.length; i = i + 1) {
    var f = this.indexOf(sFind, i);
    if (f != -1) {
       return this.substr(f + sFind.length, this.length);
       break;
    }
  }
  return this;
};
String.prototype.getLeftMost=function(sFind){
  for (var i = 0; i < this.length; i = i + 1) {
    var f = this.indexOf(sFind, i);
    if (f != -1) {
       return this.substr(0, f);
       break;
    }
  }
  return this;
};