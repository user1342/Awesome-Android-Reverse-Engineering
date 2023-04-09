
#!/bin/bash
#####################################################
#  Download Specific folders from Github using SVN
#  
#  Author: Declan Cook
#  Licence: MIT
#####################################################
GHDOMAIN="https://github.com/"
IN=$1
IN=${IN##$GHDOMAIN}
BRANCH="trunk"
FOLDER=""
IFS="/" read -a SECT <<< "$IN" 

if [[ "${SECT[3]}" != "master" ]]; then
  BRANCH=${SECT[3]}
fi
for index in "${!SECT[@]}"; do
  if [ $index -gt 3 ]; then
    FOLDER=$FOLDER/${SECT[index]}
  fi
done

# DOMAIN/USER/PROJECT/<TRUNK||BRANCH>/FOLDER
echo Exporting $GHDOMAIN${SECT[0]}/${SECT[1]}/$BRANCH$FOLDER
svn --force export $GHDOMAIN${SECT[0]}/${SECT[1]}/$BRANCH$FOLDER ./
