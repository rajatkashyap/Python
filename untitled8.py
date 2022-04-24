s='''
 <span class="indexed-biz-name">1.         <a class="biz-name js-analytics-click" data-analytics-label="biz-name" href="https://www.yelp.com/biz/guss-world-famous-fried-chicken-atlanta?osq=fried+chicken" data-hovercard-id="TdP-YvQ6PkjA7ozmInUKng"><span>Gus’s World Famous Fried Chicken</span></a>
</span>


                    </h3>
                    
                                <div class="biz-rating biz-rating-large clearfix">
                



    <div class="i-stars i-stars--regular-4 rating-large" title="4.0 star rating">
        <img class="offscreen" height="303" src="./Best Fried chicken in Atlanta, GA - Yelp_files/stars.png" width="84" alt="4.0 star rating">
    </div>


                    <span class="review-count rating-qualifier">
            549 reviews
    </span>

        </div>


                            <div class="price-category">
                <span class="bullet-after">
            
        <span class="business-attribute price-range">$$</span>
        </span>
            <span class="category-str-list">'''
print s.index('indexed-biz-name')          
print s.index('category-str-list')