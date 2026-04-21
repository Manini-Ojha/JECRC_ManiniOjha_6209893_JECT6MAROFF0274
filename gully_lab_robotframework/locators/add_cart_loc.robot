*** Variables ***
${product_card}  xpath=(//div[@class="secondary"])[2]/picture/img
${size}  xpath=//label[contains(text(),"UK 7")]
${gender}  xpath=//a[contains(text(),"WOMEN")]
${quantity}  xpath=//input[@id="Quantity-template--25420726337820__main"]
${add_to_cart}  xpath=//span[text()="Add to cart"]/parent::button
${check}  xpath=//*[text()="Check"]