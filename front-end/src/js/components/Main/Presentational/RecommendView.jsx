import React, { Fragment } from "react";
import CircularProgress from "@material-ui/core/LinearProgress";
import Grid from "@material-ui/core/Grid";
import BookInfoView from "./BookInfoView";
import { Box, makeStyles } from "@material-ui/core";

/**
 * レコメンド結果を取得する
 */
const useStyles = makeStyles(theme => ({
  box: {
    color: "white",
    margin: "3",
    textAlign: "center",
    fontSize: "30px"
  },
  progress: {
    display: "flex",
    "& > * + *": {
      marginLeft: theme.spacing(2)
    }
  }
}));

export default function RecommendView(props) {
  const classes = useStyles();
  const { error, isLoading, items } = props;

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
  } else if (isLoading === 1) {
    // ローディング時
    // TODO プログレスバー実装
    return (
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <Box className={classes.box} margin={3}>
            <div>おすすめ情報更新中</div>
          </Box>
          <CircularProgress />
        </Grid>
        {items.map(item => (
          <Fragment key={"Reco-" + items.indexOf(item)}>
            <Grid item xs={1} sm={6} md={3}>
              <BookInfoView item={item} />
            </Grid>
          </Fragment>
        ))}
      </Grid>
    );
  } else if (isLoading === 2) {
    return (
      <div>
        <Grid container spacing={3}>
          <Grid item xs={12}>
            <Box className={classes.box} margin={3}>
              <div>あなたへのおすすめ</div>
            </Box>
          </Grid>

          {items.map(item => (
            <Fragment key={"Reco-" + items.indexOf(item)}>
              <Grid item xs={1} sm={6} md={3}>
                <BookInfoView item={item} />
              </Grid>
            </Fragment>
          ))}
        </Grid>
      </div>
    );
  }
}
