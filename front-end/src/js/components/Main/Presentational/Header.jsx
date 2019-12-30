import React, { useState } from "react";
import SearchIcon from "@material-ui/icons/Search";
import {
  Button,
  makeStyles,
  AppBar,
  Toolbar,
  Typography,
  InputBase,
  fade
} from "@material-ui/core";

/**
 * ヘッダーコンポーネント
 */
const useStyles = makeStyles(theme => ({
  appBar: {
    backgroundColor: "black",
    color: "white",
    positon: "static"
  },
  title: {
    flexGrow: 1,
    display: "none",
    fontSize: "70px",
    [theme.breakpoints.up("sm")]: {
      display: "block"
    }
  },
  search: {
    position: "relative",
    borderRadius: theme.shape.borderRadius,
    backgroundColor: fade(theme.palette.common.white, 0.15),
    "&:hover": {
      backgroundColor: fade(theme.palette.common.white, 0.25)
    },
    marginLeft: 0,
    width: "100%",
    [theme.breakpoints.up("sm")]: {
      marginLeft: theme.spacing(1),
      width: "auto"
    }
  },
  SearchIcon: {
    width: theme.spacing(7),
    height: "100%",
    position: "absolute",
    pointerEvents: "none",
    display: "flex",
    alignItems: "center",
    justifyContent: "center"
  },
  inputRoot: {
    color: "inherit"
  },
  inputInput: {
    padding: theme.spacing(1, 1, 1, 7),
    transition: theme.transitions.create("width"),
    width: "100%",
    [theme.breakpoints.up("sm")]: {
      width: 120,
      "&:focus": {
        width: 200
      }
    }
  }
}));

export default function Header(props) {
  const classes = useStyles();
  const [query, setQuery] = useState("");
  const { setKeyword, handleLogout } = props;

  return (
    <AppBar className={classes.appBar}>
      <Toolbar>
        <Typography className={classes.title} variant="h1" noWrap>
          Book Reco
        </Typography>
        <div className={classes.search}>
          <div className={classes.SearchIcon}>
            <SearchIcon />
          </div>
          <InputBase
            placeholder="書籍検索..."
            classes={{
              root: classes.inputRoot,
              input: classes.inputInput
            }}
            inputProps={{ "aria-label": "search" }}
            onChange={event => setQuery(event.target.value)}
            onClick={() => setKeyword(query)}
          />
          <Button variant="contained" onClick={() => setKeyword(query)}>
            検索
          </Button>
        </div>
        <div>
          <Button color="inherit" onClick={() => handleLogout()}>
            Logout
          </Button>
        </div>
      </Toolbar>
    </AppBar>
  );
}
