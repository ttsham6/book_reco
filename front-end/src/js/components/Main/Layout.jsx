import React, { useState, useRef } from "react";
import Header from "./Presentational/Header";
import RecommendJson from "./Container/RecommendJson";
import SearchJson from "./Container/SearchJosn";
import Footer from "./Presentational/Footer";
import { Box, makeStyles, Container, Grid } from "@material-ui/core";
import User from "../Route/User";
import { Redirect } from "react-router-dom";

/**
 * 画面構成を保持するメインコンポーネント
 */
const useStyles = makeStyles(theme => ({
  root: {
    display: "flex"
  },
  content: {
    flexGrow: 1,
    height: "100vh"
  },
  container: {
    paddingTop: theme.spacing(4),
    paddingBottom: theme.spacing(4)
  },
  box: {
    padding: "0 10px",
    border: 1,
    borderRadius: 3
  }
}));

export default function Layout() {
  const classes = useStyles();
  const [keyword, setKeyword] = useState("");
  const [genre, setGenre] = useState("本");
  const recoJson = useRef(null);
  const [login, changeLogin] = useState(true);

  const handleGetReco = () => {
    recoJson.current.getNewRecommend();
  };

  const handleLogout = () => {
    User.logout();
    changeLogin(false);
  };

  if (login) {
    return (
      <div className={classes.root}>
        <main className={classes.content}>
          <Grid container spacing={6}>
            <Grid item xs={12}>
              <Header setKeyword={setKeyword} handleLogout={handleLogout} />
            </Grid>
            <Container maxWidth="lg" className={classes.container}>
              <Grid item xs={12}>
                <Box className={classes.box}>
                  {/* <div>表示テスト　レコメンド用</div> */}
                  <RecommendJson ref={recoJson} />
                </Box>
              </Grid>
              <Grid item xs={12}>
                <Box className={classes.box}>
                  {/* <div>表示テスト　検索用</div> */}
                  <SearchJson
                    handleGetReco={handleGetReco}
                    genre={genre}
                    keyword={keyword}
                  />
                </Box>
              </Grid>
            </Container>
            <Footer />
          </Grid>
        </main>
      </div>
    );
  } else {
    return <Redirect to={"/login"} />;
  }
}
