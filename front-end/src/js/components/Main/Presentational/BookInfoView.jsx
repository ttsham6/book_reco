import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import CardMedia from "@material-ui/core/CardMedia";
import Typography from "@material-ui/core/Typography";
import { CardActionArea } from "@material-ui/core";

/**
 * 書籍情報を表示するコンポーネント
 */

const useStyles = makeStyles({
  card: {
    height: 420,
    maxWidth: 345,
    padding: 20
  },
  media: {
    height: "60%",
    textAlign: "center"
  },
  content: {
    overflow: "hidden",
    whiteSpace: "nowrap",
    textOverflow: "ellipsis"
  }
});

export default function BookInfoView(props) {
  const { item } = props;
  const classes = useStyles();

  return (
    <Card className={classes.card}>
      <CardActionArea>
        <a href={item.itemUrl} target="_blank" rel="noopener noreferrer">
          <CardMedia className={classes.media}>
            <img src={item.imageUrl} alt="画像" />
          </CardMedia>
          <CardContent className={classes.content}>
            <Typography variant="h5" componet="h2">
              {item.title}
            </Typography>
            <Typography variant="body2" color="textSecondary" component="p">
              {"著者：" + item.author}
            </Typography>
            <Typography variant="body2" color="textSecondary" component="p">
              {"出版社：" + item.publisherName}
            </Typography>
            <Typography variant="body2" color="textSecondary" component="p">
              {"発売日：" + item.salesDate}
            </Typography>
            <Typography variant="body2" color="textSecondary" component="p">
              {"￥" + item.itemPrice}
            </Typography>
          </CardContent>
        </a>
      </CardActionArea>
    </Card>
  );
}
