/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
  if(s.length !== t.length){
    return false
  }
  const sMap = {}
  const tMap = {}

  for(let i=0; i<s.length; i++){
    sMap[s[i]] = (sMap[s[i]] || 0) + 1
    tMap[t[i]] = (tMap[t[i]] || 0) + 1
  }

  const sMapKeys = Object.keys(sMap)
  const tMapKeys = Object.keys(tMap)

  return sMapKeys.length === tMapKeys.length && 
    sMapKeys.every(k => sMap[k] === tMap[k])
};