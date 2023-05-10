<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        
        <xsl:variable name="identifier" select="radio-button/identifier" />
        
        <div class="container">
            <div class="form-group">

                <label class="form-check-label" >
                    <xsl:value-of select="radio-button/label"/>
                </label>
            
                <xsl:for-each select="radio-button/options/option">
                    <xsl:variable name="optionValue" select="value" />
                    <div class="form-check">
                        <input class="form-check-input" type="radio" 
                               value="{$optionValue}" 
                               name="{$identifier}" 
                               id="{$optionValue}" />
                        <label class="form-check-label" for="{$optionValue}">
                            <xsl:value-of select="value"/>
                        </label>
                    </div>            
                </xsl:for-each>
                
                <small class="form-text form-text-sm text-muted">
                    <xsl:value-of select="radio-button/tooltip"/>
                </small>
                
            </div>
        </div>
        
    </xsl:template>
</xsl:stylesheet>
