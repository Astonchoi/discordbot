### 🛠️ API Usage Summary

The base domain for the API is `https://meme-api.com`. All endpoints use the `/gimme` path.

#### 1\. Get a Single Random Meme

- **Endpoint:** `/gimme`
- **Example:** `https://meme-api.com/gimme`
- **Description:** Returns a single, random meme from a default set of popular subreddits (**'memes'**, **'dankmemes'**, **'me_irl'**).

#### 2\. Get Multiple Random Memes

- **Endpoint:** `/gimme/{count}`
- **Example:** `https://meme-api.com/gimme/3`
- **Description:** Returns a list of memes. The `{count}` can be any number up to a **maximum of 50**.

#### 3\. Get a Single Meme from a Specific Subreddit

- **Endpoint:** `/gimme/{subreddit}`
- **Example:** `https://meme-api.com/gimme/wholesomememes`
- **Description:** Returns one random meme from the specified subreddit.

#### 4\. Get Multiple Memes from a Specific Subreddit

- **Endpoint:** `/gimme/{subreddit}/{count}`
- **Example:** `https://meme-api.com/gimme/wholesomememes/5`
- **Description:** Returns a list of memes from the specified subreddit. The `{count}` can be up to a **maximum of 50**.

---

### 📦 Example Response Format

A successful request typically returns a JSON object containing details about the meme(s), including the direct image **`url`** and the Reddit post link **`postLink`**.

```json
{
  "postLink": "https://redd.it/...",
  "subreddit": "dankmemes",
  "title": "A funny title",
  "url": "https://i.redd.it/...", // Direct link to the image/gif
  "nsfw": false,
  "spoiler": false,
  "author": "UserName",
  "ups": 1234,
  "preview": [...] // Array of lower-quality preview images
}
```
