import React from "react";
import { Button, TextField, makeStyles, Box } from "@material-ui/core/";

/**
 * 検索フォームコンポーネント
 */

const useStyles = makeStyles({
  form: {
    paddingLeft: "10"
  },
  formText: {
    backgroundColor: "white"
  }
});

export default function SearchForm(props) {
  const classes = useStyles();
  const { setKeyword, execSearch } = props;
  return (
    <Box className={classes.fomr} position="static">
      <TextField
        className={classes.formText}
        id="outlined-search"
        type="search"
        variant="outlined"
        onChange={event => setKeyword(event.target.value)}
      />
      <Button variant="contained" onClick={() => execSearch()}>
        検索
      </Button>
    </Box>
  );
}
