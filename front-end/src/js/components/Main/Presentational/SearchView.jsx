import React, { Fragment } from "react";
import BookInfoView from "./BookInfoView";
import { Grid, Box, makeStyles } from "@material-ui/core";
import CircularProgress from "@material-ui/core/LinearProgress";

const useStyles = makeStyles({
  box: {
    color: "white",
    margin: "3",
    textAlign: "center",
    fontSize: "30px"
  }
});

export default function SearchView(props) {
  const { error, isLoading, items } = props;
  const classes = useStyles();

  if (error) {
    // エラー発生時
    // TODO エラー処理実装
    return (
      <div>
        <Box className={classes.box} margin={3}>
          <div>Error: {error.message}</div>
        </Box>
      </div>
    );
  } else if (isLoading === 0) {
    return null;
    // return <div>検索条件を入力してください</div>;
  } else if (isLoading === 1) {
    return (
      // ローディング時
      // TODO プログレスバー実装
      <div>
        <Box className={classes.box} margin={3}>
          <div>検索中</div>
        </Box>
        <CircularProgress />
      </div>
    );
  } else if (isLoading === 2) {
    return (
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <Box className={classes.box} margin={3}>
            <div>検索結果</div>
          </Box>
        </Grid>
        {items.map(item => (
          <Fragment key={"Reco-" + items.indexOf(item)}>
            <Grid item xs={3} sm={6} md={3}>
              <BookInfoView item={item} />
            </Grid>
          </Fragment>
        ))}
      </Grid>
    );
  }
}
