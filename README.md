# nft-collection-concept
Computer generated "artwork" to conceptualize the creation of an NFT collection, for fun

Planned roadmap:

1. Create a collection of unique digital pieces of abstract "artwork" using python drawing libraries.
2. Split the pieces up into 3x3 sections and create 4 variations of each section which have been rotated 90 degrees.
3. Apply a level of rarity to each piece, dependent on chronological order of creation.
4. Generate the final collection by randomly stitching together unique combinations of the pieces.
5. Integrate the collection with an NFT network

The level of rarity of a particular piece will be determined by the sum of all 9 component pieces.

Each component will have a rarity = 1/x * 1000 * (a rotation factor) * (a piece index factor), where x is the index of the order of creation.
Since each piece has 3 other rotated pieces, the rarity of each piece will follow: [1, 1/3, 1/3, 2/3] where 90 degree rotated pieces are 1/3 the rarity of the original piece, and 180 degree rotated pieces are 2/3 the rarity of the original piece.

### First generated collection. Pre-split
![image](https://user-images.githubusercontent.com/69197760/140965241-1b179c55-ed0f-4aa8-9685-f9700c412be2.png)

### Post split

![image](https://user-images.githubusercontent.com/69197760/140988877-fb50613c-48dd-4c87-a02e-93d46de5544e.png)

### Final stitched images

![image](https://user-images.githubusercontent.com/69197760/141021515-0c26ac33-6943-4029-ad18-2f930f7ac320.png)

### Collection 2

![circasso66](https://user-images.githubusercontent.com/69197760/141105627-a6455504-eba5-4b09-b7cd-219ba56d9a6e.jpeg)
